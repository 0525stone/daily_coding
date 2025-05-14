"""
250421 Test 하는 Raw 한 코드들 여기에 추가해서 정리할 예정..

Debug 모드를 코드로 따로 구현하고 싶음
    Debug 모드의 경우, 어떤 특징검출기를 쓰고, 어떤 파라미터 값을 적용한지 중간중간 혹은 전체 브리핑해주게
        - 그렇게 하려면 Dict 형 데이터를 쓰면 되나?

"""
from utils import lys_opencv as utop
from utils import lys_file as ut

import os
import cv2
import numpy as np


def test_main():
    # 카메라 내부 파라미터 (예시)
    K = np.array([[1000, 0, 320], [0, 1000, 240], [0, 0, 1]])

    # Preparation of Images
    img_root = "data/exp001"
    img1_name = "0.png"
    img2_name = "1.png"

    img1_dir = os.path.join(img_root, img1_name)
    img2_dir = os.path.join(img_root, img2_name)

    img_savedir = os.path.join(img_root, "result")
    if not os.path.exists(img_savedir):
        os.makedirs(img_savedir)
    result_name_part1 = os.path.basename(img1_name).split(".")[0]
    result_name_part2 = os.path.basename(img2_name).split(".")[0]

    result_name = f"result_{result_name_part1}_{result_name_part2}.png"
    result_dir = os.path.join(img_savedir, result_name)

    # 두 이미지 로드
    img1 = cv2.imread(img1_dir, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_dir, cv2.IMREAD_GRAYSCALE)

# 검출기 기준으로 함수 만들어서 정리 가능할 듯
#   다른 검출기들도 같은 형식으로 호출하고 사용함함
    ### 예전 버전전
    # # ORB 검출기 생성
    # orb = cv2.ORB_create()

    # # 키 포인트와 설명자 검출
    # kp1, des1 = orb.detectAndCompute(img1, None)
    # kp2, des2 = orb.detectAndCompute(img2, None)


#   다른 검출기 편하게 호출하는 버전
    detector_type = "ORB" # ORB, BRISK, AKAZE, SIFT
    detector, norm_type = utop.create_detector(detector_type)

    kp1, des1 = detector.detectAndCompute(img1, None)
    kp2, des2 = detector.detectAndCompute(img2, None)


    # BFMatcher 객체 생성
    bf = cv2.BFMatcher(norm_type, crossCheck=False)

    # knnMatch 실행
    matches = bf.knnMatch(des1, des2, k=2)

    # Lowe's ratio test     # TODO : 이거 뭔지 확인 필요
    lowe_ratio = 0.5  # NOTE
    good_matches = []
    for match in matches:
        if len(match) == 2:
            if match[0].distance < lowe_ratio * match[1].distance:
                good_matches.append(match[0])

    print(f"The number of good matches :  {len(good_matches)}")
# 함수 정리 완료
    # 기본 행렬과 본질 행렬 계산
    E, mask = utop.find_fundamental_essential_matrix(good_matches, kp1, kp2, K)

    # 본질 행렬 분해
    R1, R2, t = utop.decompose_essential_matrix(E)

    # 카메라 간 각도 계산
    angle = utop.calculate_angle_between_cameras(R1)
    print(f"Estimated angle between cameras: {angle} degrees")

    # 그림 그려준 결과
    good_matches = utop.find_good_matches(des1, des2)

    # 매칭 결과 그리기
    utop.draw_matches(img1, kp1, img2, kp2, good_matches, result_dir)

if __name__=="__main__":
    # dirname1 = "data/data_gg/fmvs/Anode_Coater_Line_1"
    # filelist1 = ut.list_from_dir(dirname1)

    # dirname2 = "data/data_gg/fmvs/Anode_Coater_Line_2"
    # filelist2 = ut.list_from_dir(dirname2)

    # dirname3 = "data/data_gg/fmvs/Anode_Coater_Line_3"
    # filelist3 = ut.list_from_dir(dirname3)

    # dirname4 = "data/data_gg/fmvs/Anode_Coater_Line_4"
    # filelist4 = ut.list_from_dir(dirname4)

    test_main()
