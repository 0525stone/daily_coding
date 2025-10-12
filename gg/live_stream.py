import cv2
import numpy as np
import pytesseract

# --- 알고리즘 1: Grayscale 변환 ---
def algorithm1_gray(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# --- 알고리즘 2: Gaussian Blur ---
def algorithm2_blur(frame):
    return cv2.GaussianBlur(frame, (5, 5), 0)

# --- 모션 디텍션: 프레임 차이 기반 ---
class MotionDetector:
    def __init__(self):
        self.prev = None

    def __call__(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self.prev is None:
            self.prev = gray
            return np.zeros_like(gray)

        diff = cv2.absdiff(self.prev, gray)
        self.prev = gray
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        return thresh

# --- YOLO 객체 탐지 ---
class YOLODetector:
    def __init__(self):
        self.net = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        self.classes = open("coco.names").read().strip().split('\n')

    def __call__(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)

        height, width = frame.shape[:2]
        boxes, confidences, class_ids = [], [], []

        for output in outputs:
            for det in output:
                scores = det[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x, center_y, w, h = (det[0:4] * np.array([width, height, width, height])).astype(int)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = self.classes[class_ids[i]]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        return frame

# --- OCR (문자 인식) ---
def ocr_read(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    if text.strip():
        print("OCR Text:", text.strip())
    return frame

# --- 알고리즘 리스트 ---
ALGORITHMS = [
    ("Gray", algorithm1_gray),
    ("Blur", algorithm2_blur),
    ("Motion", MotionDetector()),
    ("YOLO", YOLODetector()),
    ("OCR", ocr_read),
]

# --- 메인 루프 ---
def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        temp_frame = frame.copy()
        for name, func in ALGORITHMS:
            output = func(temp_frame)
            cv2.imshow(name, output)
            temp_frame = output  # 다음 알고리즘에 넘김

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
