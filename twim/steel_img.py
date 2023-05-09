import cv2
import copy
import numpy as np

class steel_img():
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

    # # ==================================================================================================================
    # FIXME : class로 분리 필요
    # defect 부분 => 따로 class로 빼면 될 듯
    def blob(self, blob_size=10, blob_area_width=5, blob_ref=6):
        self.defect_th = 0 # 밝기 값의 차이에 대한 threshold
        self.blob_size = blob_size
        self.blob_area_width = blob_area_width
        self.blob_area_height = self.dst_height//self.blob_size
        self.blob_ref = blob_ref

        self.ref_blob = []

    # def crop_blob(self):
    #     self.crop_img_left = copy.deepcopy(self.dst_img)[:self.blob_w,:]
    #     self.crop_img_right = copy.deepcopy(self.dst_img)[-self.blob_w:,:]
    #     self.crop_img = cv2.hconcat([self.crop_img_left, self.crop_img_right])
    #     self.show_img = self.crop_img

    def grid_blob(self):
        pass

    # def draw_blob(self):
    #     self.blob_img = cv2.line(self.dst_img, (self.blob_w*self.blob_size,0), (self.blob_w*self.blob_size, self.dst_height),color=(0,255,0),thickness=2)
    #     self.blob_img = cv2.line(self.dst_img, (self.dst_width-self.blob_w*self.blob_size,0), (self.dst_width-self.blob_w*self.blob_size, self.dst_height),color=(0,255,0),thickness=2)
    #     self.show_img = self.blob_img

    def make_blob_img(self):
        """
        기존 dst_img(W x H) 를 blob_img(blob_w x blob_h) 로 만들어버림
        """
        w,h = self.dst_img.shape[0], self.dst_img.shape[1]
        self.blob_img = np.zeros([self.blob_area_width*2, self.blob_area_height]) # width = left blob & ref, right blob & ref
        self.blob_defect = np.zeros(self.blob_img.shape) 
        self.blob_ref_img = np.zeros([2, self.blob_area_height])

        for j in range(self.blob_area_height):
            mean_blob_ref_left = np.mean(self.dst_img[self.blob_size*self.blob_area_width+1:self.blob_size*self.blob_area_width+1+self.blob_ref,j*self.blob_size:(j+1)*self.blob_size])
            mean_blob_ref_right = np.mean(self.dst_img[-1-self.blob_area_width*self.blob_size:-1-self.blob_area_width*self.blob_size-self.blob_ref:-1,j*self.blob_size:(j+1)*self.blob_size])
            self.blob_ref_img[0][j] = mean_blob_ref_left
            self.blob_ref_img[1][j] = mean_blob_ref_right
            for i in range(self.blob_area_width):
                temp_blob_left = np.mean(self.dst_img[i*self.blob_size:(i+1)*self.blob_size,j*self.blob_size:(j+1)*self.blob_size])
                temp_blob_right = np.mean(self.dst_img[-1-i*self.blob_size:-1-(i+1)*self.blob_size:-1,j*self.blob_size:(j+1)*self.blob_size])
                self.blob_img[i][j] = temp_blob_left
                self.blob_img[-i-1][j] = temp_blob_right
                if temp_blob_left-mean_blob_ref_left>self.defect_th:
                    self.blob_defect[i][j]=1
                if temp_blob_right-mean_blob_ref_right>self.defect_th:
                    self.blob_defect[-i-1][j]=1
        print()

    def get_blob_ref(self):
        """
        ref로 잡은 영역에 대해서는 불량이 없다는 것을 전제하에 reference 밝기 값을 구하는 것이 의미가 있음
        """
        print()
        # self.ref_blob [0]에 left [1]에 right
        
        # blob_left = []
        # blob_right = []
        # for i in range(self.)


def perspective_transform(src_img, src_pts, width, height):
    """
    width, height 는 transform 한 결과에 대한 사이즈(not img 사이즈)
    """
    dst_pts = np.float32([[0,0], [width,0], [0, height], [width, height]])

    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    dst = cv2.warpPerspective(src_img, M, (width, height))
    return dst


def main():

    # TODO : edge.cs 보고 구현해놓기
    


    # 합판 변환 후, 
    img_dir = "data/test_3669.png"
    # 진짜 꼭지점들
    top_left = (127,355)
    top_right = (1687, 381)
    bottom_left = (103,1079)
    bottom_right = (1681,1079)

    # # 동작 확인용
    # src_img = cv2.imread("data/test_3669.png")
    # top_left = (107,341)
    # top_right = (1697,365)
    # bottom_left = (85,1079)
    # bottom_right = (1695,1079)

    input_pts = [top_left, top_right, bottom_left, bottom_right]

    # dst_img = perspective_transform(src_img, input_pts, width=1920 , height=1080)

    st = steelimg(img_dir=img_dir, src_pts=input_pts)
    st.transform()
    st.concat_src_dst()
    # st.show()

    # # ================================================================================================
    print("blob")
    st.blob()
    st.make_blob_img() 
    # st.draw_blob()
    # st.grid_blob()
    # st.get_blob_ref()
    # st.show()
    

if __name__=="__main__":
    main()