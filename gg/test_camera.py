import os
import cv2

# 웹캠을 열기 (기본 웹캠은 인덱스 0)
cap = cv2.VideoCapture(0)

# 웹캠이 열렸는지 확인
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    exit()

# 저장을 위한 변수들
save_idx = 0
save_dir = "./data/result"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 비디오 읽기 및 표시 루프
while True:
    ret, frame = cap.read()
    if not ret:
        print("프레임을 읽을 수 없습니다.")
        break
    
    # 프레임을 윈도우에 표시
    cv2.imshow('Logitech Brio', frame)
    
    # 'q' 키를 누르면 루프 종료
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        savename = os.path.join(save_dir,f"{save_idx}.png")
        save_idx+=1
        cv2.imwrite(savename, frame) 

# 웹캠 및 윈도우 해제
cap.release()
cv2.destroyAllWindows()