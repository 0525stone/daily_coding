from flask import Flask, Response
import cv2
"""
250118 Flask server test

TODO
- 같은 망이 아닌 외부망에서도 접속할 수 있게 하려면 어떤 설정이 필요한지
- 쿠버네티스 구성
  - API 로 만들어서 쿠버네티스에 올리는 방법

"""

# Flask 앱 생성
app = Flask(__name__)

# 웹캠 초기화
camera = cv2.VideoCapture(0)  # 0은 기본 웹캠, 필요시 다른 숫자로 변경

def generate_frames():
    while True:
        # 웹캠에서 프레임 읽기
        success, frame = camera.read()
        if not success:
            break
        else:
            # 프레임을 JPEG로 인코딩
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            # 멀티파트 응답 형식으로 프레임 반환
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # 비디오 피드를 스트리밍으로 반환
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    # Flask 서버 실행
    app.run(host='0.0.0.0', port=5000, debug=True)
