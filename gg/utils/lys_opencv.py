"""
Functions
- find_fundamental_essential_matrix
- decompose_essential_matrix
- calculate_angle_between_cameras
- find_good_matches
- draw_matches


"""
import cv2
from utils import lys_file as ut
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

def draw_matches(img1, kp1, img2, kp2, matches, savename):
    # 매칭 결과를 그래픽으로 표시
    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow('Matches', img_matches)
    if not savename:
        cv2.imwrite('data/result_jh.jpg', img_matches)
    else:
        cv2.imwrite(savename, img_matches)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# GPT 권유해준 코드
def create_detector(detector_type):
    if detector_type == "ORB":
        return cv2.ORB_create(), cv2.NORM_HAMMING
    elif detector_type == "BRISK":
        return cv2.BRISK_create(), cv2.NORM_HAMMING
    elif detector_type == "AKAZE":
        return cv2.AKAZE_create(), cv2.NORM_HAMMING
    elif detector_type == "SIFT":
        return cv2.SIFT_create(), cv2.NORM_L2
    else:
        raise ValueError(f"Unsupported detector: {detector_type}")

def test_main():
    # 카메라 내부 파라미터 (예시)
    K = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]])

    # 두 이미지 로드
    img1 = cv2.imread("data/result/0.png", cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread("data/result/1.png", cv2.IMREAD_GRAYSCALE)

# 검출기 기준으로 함수 만들어서 정리 가능할 듯
#   다른 검출기들도 같은 형식으로 호출하고 사용함함
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

# 함수 정리 완료
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

if __name__=="__main__":
    dirname1 = "data/data_gg/fmvs/Anode_Coater_Line_1"
    filelist1 = ut.list_from_dir(dirname1)

    dirname2 = "data/data_gg/fmvs/Anode_Coater_Line_2"
    filelist2 = ut.list_from_dir(dirname2)

    dirname3 = "data/data_gg/fmvs/Anode_Coater_Line_3"
    filelist3 = ut.list_from_dir(dirname3)

    dirname4 = "data/data_gg/fmvs/Anode_Coater_Line_4"
    filelist4 = ut.list_from_dir(dirname4)

    # test_main()
