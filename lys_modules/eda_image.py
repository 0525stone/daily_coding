"""
Exploratory Data Analysis for Image data
- read image
- draw line
- draw circle(point)
"""
import os
import cv2


class VP:
    """
    객체를 만들고 해당 객체에 이미지와 다른 정보(선, 점)가 들어오면 그린 결과를 출력으로 내보내줌
    """
    def __init__(self,filename):
        self.img = cv2.imread(filename)

    def draw_line(self, pt1, pt2):
        # cv2.line(self.img, (pt1, pt2))
        pass
    
    def show(self, windowname="result"):
        cv2.imshow("result", self.img)
        cv2.waitKey(-1) # TODO : 입력 키에 따라서 저장할지 넘길지에 대한 옵션도 줄 수 있음

def main():
    print("EDA")
    filename = "/Users/johnlee/git/daily_coding/data/gt/2311.jpg"
    vp = VP(filename)
    vp.show()
    

if __name__=="__main__":
    main()
    """
    참조
    - 

    """