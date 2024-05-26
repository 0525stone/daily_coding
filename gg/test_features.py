import os
import cv2
import numpy as np

# 이미지 불러오기
image_path = "data/result/0.png"  # 처리할 이미지 파일 경로를 입력하세요
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("이미지를 불러올 수 없습니다.")
    exit()

# 결과를 시각화할 윈도우 이름 목록
window_names = ['FAST Keypoints', 'SIFT Keypoints', 'SURF Keypoints', 'BRISK Keypoints', 'ORB Keypoints']
save_dir = './data/result'
filename = image_path.split('/')[-1].split('.')[0]

# 1. FAST
fast_name = 'FAST'
fast = cv2.FastFeatureDetector_create()
keypoints_fast = fast.detect(image, None)
image_fast = cv2.drawKeypoints(image, keypoints_fast, None, color=(0, 255, 0))
cv2.imshow(window_names[0], image_fast)
savename = os.path.join(save_dir, f"{filename}_{fast_name}.png")
cv2.imwrite(savename, image_fast)


# 2. SIFT
sift_name = 'SIFT'
sift = cv2.SIFT_create()
keypoints_sift, _ = sift.detectAndCompute(image, None)
image_sift = cv2.drawKeypoints(image, keypoints_sift, None, color=(0, 255, 0))
cv2.imshow(window_names[1], image_sift)
savename = os.path.join(save_dir, f"{filename}_{sift_name}.png")
cv2.imwrite(savename, image_sift)


# # 3. SURF (참고: SURF는 상용 알고리즘으로, OpenCV contrib 패키지가 필요합니다)
# surf = cv2.xfeatures2d.SURF_create()
# keypoints_surf, _ = surf.detectAndCompute(image, None)
# image_surf = cv2.drawKeypoints(image, keypoints_surf, None, color=(0, 255, 0))
# cv2.imshow(window_names[2], image_surf)

# 4. BRISK
brisk_name = 'BRISK'
brisk = cv2.BRISK_create()
keypoints_brisk, _ = brisk.detectAndCompute(image, None)
image_brisk = cv2.drawKeypoints(image, keypoints_brisk, None, color=(0, 255, 0))
cv2.imshow(window_names[3], image_brisk)
savename = os.path.join(save_dir, f"{filename}_{brisk_name}.png")
cv2.imwrite(savename, image_brisk)



# 5. ORB
orb_name = 'ORB'
orb = cv2.ORB_create()
keypoints_orb, _ = orb.detectAndCompute(image, None)
image_orb = cv2.drawKeypoints(image, keypoints_orb, None, color=(0, 255, 0))
cv2.imshow(window_names[4], image_orb)
savename = os.path.join(save_dir, f"{filename}_{orb_name}.png")
cv2.imwrite(savename, image_orb)



# 모든 윈도우 표시 및 키 입력 대기
cv2.waitKey(0)
cv2.destroyAllWindows()
