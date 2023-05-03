"""
Exploratory Data Analysis for Image data
- read image
- draw line
- draw circle(point)
"""
import os
import cv2
import json
import numpy as np

class VP:
    """
    객체를 만들고 해당 객체에 이미지와 다른 정보(선, 점)가 들어오면 그린 결과를 출력으로 내보내줌
    """
    def __init__(self,filename):
        self.img = cv2.imread(filename)
        self.filename = '/'.join(filename.split(".")[:-1])
        print(self.filename)
        self.json = f"{self.filename}_camera.json"
        self.npz = f"{self.filename}_label.npz"
        self.jlk = f"{self.filename}.jlk"
        self.focal_length = 2.1875

    def read_infos(self):
        """
        못 읽으면 못읽었다는 에러 메세지 내뱉게 하고 싶은데..
        """
        try:
            with open(self.json, "r") as st_json:
                self.json_data = json.load(st_json)
                print(self.json_data)
            self.npz_data = np.load(self.npz)
        except:
            print("some file cannot be read")

    def to_pixel(self, vpts, focal_length=1.0, h=512, w=512): # 기존 h=480, w=640
        x = vpts[:,0] / vpts[:, 2] * focal_length * max(h, w)/2.0 + w//2
        y = -vpts[:,1] / vpts[:, 2] * focal_length * max(h, w)/2.0 + h//2
        return y, x

    def get_vps(self):
        try:
            vpts = self.npz_data['vpts']
            self.vpts_y,self.vpts_x = self.to_pixel(vpts, focal_length=self.focal_length)
            return True
        except:
            print("no npz file information")
            return False
        

    def draw_line(self, pt1, pt2):
        # cv2.line(self.img, (pt1, pt2))
        pass

    def draw_point(self, x, y):
        """
        외부에서 읽은 점으로 찍어보는 것 가능
        parameter로 cv2.circle 관련 파라미터 받는 것도 좋을 듯
        """
        if x<
        pass
    
    def show(self, windowname="result"):
        cv2.imshow("result", self.img)
        cv2.waitKey(-1) # TODO : 입력 키에 따라서 저장할지 넘길지에 대한 옵션도 줄 수 있음
        cv2.destroyAllWindows()

def main():
    """
    su3 를 기준으로 vanishing point 확인하는 코드 필요
    """
    print("EDA")
    filename = "/Users/johnlee/git/daily_coding/data/su3/002_0085_0.png"
    vp = VP(filename)
    vp.read_infos()
    vpts_exist = vp.get_vps()
    if vpts_exist:
        for i in range(len(vp.vpts_x)):
            vp.draw_point(vp.vpts_x[i],vp.vpts_y[i])
    # vp.show()
    

if __name__=="__main__":
    main()
    """
    참조
    - 

    """