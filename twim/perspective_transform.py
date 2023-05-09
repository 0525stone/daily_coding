import cv2
import numpy as np

class steelimg():
    def __init__(self, img_dir, src_pts, width=1290, height=1080):
        self.img_dir = img_dir
        self.src_pts = src_pts
        self.width = width
        self.height = height


def perspective_transform(src_img, src_pts, width, height):
    """
    width, height 는 transform 한 결과에 대한 사이즈(not img 사이즈)
    """
    src_pts = np.float32([src_pts[0], src_pts[1], src_pts[2], src_pts[3]])
    dst_pts = np.float32([[0,0], [width,0], [0, height], [width, height]])

    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    dst = cv2.warpPerspective(src_img, M, (width, height))
    return dst


def main():

    src_img = cv2.imread("data/test_3669.png")

    # # 진짜 꼭지점들
    # top_left = (127,355)
    # top_right = (1687, 381)
    # bottom_left = (103,1079)
    # bottom_right = (1681,1079)

    # 확인용
    top_left = (107,341)
    top_right = (1697,365)
    bottom_left = (85,1079)
    bottom_right = (1695,1079)

    input_pts = [top_left, top_right, bottom_left, bottom_right]

    dst_img = perspective_transform(src_img, input_pts, width=1920 , height=1080)

    if 1:
        for p in input_pts:
            src_img = cv2.circle(src_img,(p[0],p[1]), radius=4,color=(0,255,0), thickness=3)

    show_img = cv2.hconcat([src_img, dst_img])
    # show_img = dst_img
    # show_img = src_img
    cv2.imshow("result", show_img)
    cv2.waitKey(-1)
    cv2.imwrite("data/result.png",show_img)

if __name__=="__main__":
    main()