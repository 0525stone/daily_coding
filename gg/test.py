import cv2
import numpy as np

def find_fundamental_essential_matrix(matches, kp1, kp2, K):
    # 매칭된 키 포인트 위치 추출
    points1 = np.float32([kp1[m.queryIdx].pt for m in matches])
    points2 = np.float32([kp2[m.trainIdx].pt for m in matches])

    # 기본 행렬 계산
    F, mask = cv2.findFundamentalMat(points1, points2, cv2.FM_RANSAC)
    # 본질 행렬 계산
    E = K.T @ F @ K

    return E, mask

def decompose_essential_matrix(E):
    # SVD를 사용하여 본질 행렬 분해
    U, _, Vt = np.linalg.svd(E)
    W = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])

    # 첫 번째 가능한 회전 행렬과 두 번째 가능한 회전 행렬
    R1 = U @ W @ Vt
    R2 = U @ W.T @ Vt

    # 이동 벡터
    t = U[:, 2]

    # 회전 행렬의 부호 보정
    if np.linalg.det(R1) < 0:
        R1 = -R1
    if np.linalg.det(R2) < 0:
        R2 = -R2

    return R1, R2, t


def calculate_angle_between_cameras(R):
    # 회전 행렬의 트레이스가 [-1, 3] 범위 내에 있는지 보장
    trace_value = np.clip((np.trace(R) - 1) / 2, -1.0, 1.0)
    theta_rad = np.arccos(trace_value)
    theta_deg = np.degrees(theta_rad)
    return theta_deg

def find_good_matches(des1, des2):
    # BFMatcher 객체 생성
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    # knnMatch 실행
    matches = bf.knnMatch(des1, des2, k=2)
    # Lowe's ratio test를 통해 좋은 매치 필터링
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)
    return good_matches

def draw_matches(img1, kp1, img2, kp2, matches):
    # 매칭 결과를 그래픽으로 표시
    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow('Matches', img_matches)
    cv2.imwrite('data/result_jh.jpg', img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 카메라 내부 파라미터 (예시)
K = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]])

# 두 이미지 로드
img1 = cv2.imread("data/result/0.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("data/result/1.png", cv2.IMREAD_GRAYSCALE)

# ORB 검출기 생성
orb = cv2.ORB_create()

# 키 포인트와 설명자 검출
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# BFMatcher 객체 생성
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

# knnMatch 실행
matches = bf.knnMatch(des1, des2, k=2)

# Lowe's ratio test
good_matches = []
for match in matches:
    if match[0].distance < 0.75 * match[1].distance:
        good_matches.append(match[0])
# 기본 행렬과 본질 행렬 계산

E, mask = find_fundamental_essential_matrix(good_matches, kp1, kp2, K)

# 본질 행렬 분해
R1, R2, t = decompose_essential_matrix(E)

# 카메라 간 각도 계산
angle = calculate_angle_between_cameras(R1)
print(f"Estimated angle between cameras: {angle} degrees")

# 그림 그려준 결과
good_matches = find_good_matches(des1, des2)

# 매칭 결과 그리기
draw_matches(img1, kp1, img2, kp2, good_matches)