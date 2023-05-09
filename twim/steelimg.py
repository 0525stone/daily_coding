import cv2
import copy
import numpy as np

class steelimg():
    def __init__(self, img_dir, src_pts, dst_width=1290, dst_height=1080):
        self.img_dir = img_dir
        self.src_pts = src_pts
        self.dst_width = dst_width
        self.dst_height = dst_height

        # 필요한 데이터
        self.src_img = cv2.imread(self.img_dir)
        self.src_pts = np.float32([self.src_pts[0], self.src_pts[1], self.src_pts[2], self.src_pts[3]])
        self.dst_pts = np.float32([[0,0], [dst_width,0], [0, dst_height], [dst_width, dst_height]])

        self.show_img = copy.deepcopy(self.src_img)

    def transform(self):
        self.M = cv2.getPerspectiveTransform(self.src_pts, self.dst_pts)
        self.dst_img = cv2.warpPerspective(self.src_img, self.M, (self.dst_width, self.dst_height))

    def concat_src_dst(self):
        self.show_img = cv2.hconcat([self.src_img, self.dst_img])

    def show(self, window="result"):
        cv2.imshow(window,self.show_img)
        cv2.waitKey(-1)

    def save(self, savename="result.png"):
        cv2.imwrite(savename, self.show_img)
    
    def show_save(self):
        self.show()
        self.save()

    # defect 부분
    def blob(self, blob_size=10, table_width=5):
        self.blob_size = blob_size
        self.blob_h = self.dst_height//self.blob_size
        self.blob_w = table_width

    # def crop_blob(self):
    #     self.crop_img_left = copy.deepcopy(self.dst_img)[:self.blob_w,:]
    #     self.crop_img_right = copy.deepcopy(self.dst_img)[-self.blob_w:,:]
    #     self.crop_img = cv2.hconcat([self.crop_img_left, self.crop_img_right])
    #     self.show_img = self.crop_img

    def grid_blob(self):
        pass

    def draw_blob(self):
        self.blob_img = cv2.line(self.dst_img, (self.blob_w*self.blob_size,0), (self.blob_w*self.blob_size, self.dst_height),color=(0,255,0),thickness=2)
        self.blob_img = cv2.line(self.dst_img, (self.dst_width-self.blob_w*self.blob_size,0), (self.dst_width-self.blob_w*self.blob_size, self.dst_height),color=(0,255,0),thickness=2)
        self.show_img = self.blob_img

def perspective_transform(src_img, src_pts, width, height):
    """
    width, height 는 transform 한 결과에 대한 사이즈(not img 사이즈)
    """
    dst_pts = np.float32([[0,0], [width,0], [0, height], [width, height]])

    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    dst = cv2.warpPerspective(src_img, M, (width, height))
    return dst


def main():

    
    src_img = cv2.imread("data/test_3669.png")

    img_dir = "data/test_3669.png"
    # 진짜 꼭지점들
    top_left = (127,355)
    top_right = (1687, 381)
    bottom_left = (103,1079)
    bottom_right = (1681,1079)

    # # 동작 확인용
    # top_left = (107,341)
    # top_right = (1697,365)
    # bottom_left = (85,1079)
    # bottom_right = (1695,1079)

    input_pts = [top_left, top_right, bottom_left, bottom_right]

    # dst_img = perspective_transform(src_img, input_pts, width=1920 , height=1080)

    st = steelimg(img_dir=img_dir, src_pts=input_pts)
    st.transform()
    st.concat_src_dst()
    st.show()

    print("blob")
    st.blob()
    st.draw_blob()
    st.grid_blob()
    st.show()
    

    # if 1:
    #     for p in input_pts:
    #         src_img = cv2.circle(src_img,(p[0],p[1]), radius=4,color=(0,255,0), thickness=3)

    # show_img = cv2.hconcat([src_img, dst_img])
    # cv2.imshow("result", show_img)
    # cv2.waitKey(-1)
    # cv2.imwrite("data/result.png",show_img)

if __name__=="__main__":
    main()