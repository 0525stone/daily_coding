"""
AA 그리는 것도 염두해둬야함

더 나은 구조는 vp_metric 하는 클래스 두고 상위에 데이터셋별 클래스를 두는 것임...
su3
"""
import os
import cv2

# from tqdm import tqdm
import math
import numpy as np
import matplotlib.pyplot as plt


class Su3():
    def __init__(self, ground_truth_root, result_root):
        self.gt_root = ground_truth_root # TODO : 데이터에 대한 객체를 만들어야하나?
        self.result_root = result_root

        # 필요 파라미터들
        self.gt_format = '.npz' # '.json' TODO : json에 대해서도 읽을 수 있게 해야함ㄴ
        self.gt_img_format = '.png'
        self.img_ok = False # False True

        # points 정보들 들고 있어야하나?
        self.gt_pts = [] # 몇만개의 데이터에 대해서 갖고 있게끔 하는게 맞을까? 그때 그때 읽어서 하는게 나을듯
        self.result_pts = []

        self.degree_list = []

        self.init_data()
        # self.loop_files()

    def summary(self):
        print(f"Ground truth root : {self.gt_root} files : {len(self.gt_files)}")
        print(f"result root : {self.result_root} files : {len(self.result_files)}")
        print()

    def init_data(self):
        self.gt_files = []
        self.gt_img_files = []
        self.result_files = sorted(os.listdir(self.result_root))
        # gt 파일들은 경로를 불러오는데 방법이 필요함 => 결과 파일명에서 경로를 따로 따내서 해야함
        for f in self.result_files:
            filename = os.path.basename(f)
            f_dir = filename.split('_')[0]
            fname = '_'.join(os.path.basename(f).split('_')[1:]).split('.')[0]
            if self.gt_format=='.npz':
                gt_filename = f"{self.gt_root}/{f_dir}/{fname}_label{self.gt_format}"
                gt_img_filename = f"{self.gt_root}/{f_dir}/{fname}{self.gt_img_format}"
            elif self.gt_format=='.json': 
                gt_filename = f"{self.gt_root}/{f_dir}/{fname}_camera{self.gt_format}"
                gt_img_filename = f"{self.gt_root}/{f_dir}/{fname}{self.gt_img_format}"
            self.gt_files.append(gt_filename)
            self.gt_img_files.append(gt_img_filename)
                
    def process_total_data(self):
        self.degree_list = []
        for idx, (gt, result) in enumerate(zip(self.gt_files, self.result_files)): # FIXME : gt, result없이 그냥 idx만 읽게 해도됨
            assert gt!=result, f"{gt}\t{result}"
            # if idx<2000:
            # FIXME : 예외처리해야함. 파일 만약에 없는 경우...
            gt_pt, result_pt = self.__read_data(idx) # TODO : idx로 img를 불러오려면.. 
            degree, gt_pt, result_pt = self.process_data(gt_pt, result_pt)
            self.degree_list.append(degree)
            if degree<90:
                if self.img_ok:
                    self.check_img(idx, gt_pt, result_pt, degree)
        print("================================")
        print(f"result : {len(self.degree_list)}")
        return self.degree_list
    
    def process_data(self, gt_pt, result_pt):
        # 이 함수만 따로 쓸 수 있게 인자를 줘서 실행하게끔.. 전역변수로 프로그램 실행하는 것은 안좋dma
        degree, gt = self.__compare_degree(gt_pt, result_pt)
        # print(f"gt : {gt}\tpred : {result_pt}\ndegree : {degree}\n")
        return degree, gt, result_pt
    
    def process_total_result(self):
        # TODO : AA accuracy 구하기
        self.AA_graph(self.degree_list)

    def AA_graph(self, degree_list, AA_upper_th=20):
        aa_list = []
        th_list = []
        degree_list = sorted(degree_list)
        for th in range(0,AA_upper_th*10,1):
            th_ = th/10
            for idx, deg in enumerate(degree_list):
                if deg>th_: 
                    # aa = (len(degree_list)-idx)/len(degree_list)
                    aa = (idx)/len(degree_list)
                    th_list.append(th_)
                    aa_list.append(aa)
                    break
                elif idx==len(degree_list)-1:
                    th_list.append(th_)
                    aa_list.append(1)
        plt.plot(th_list, aa_list, label=f"result")

        print(f"AA@1 eq : {self._AA(th_list, aa_list, 1)}")
        print(f"AA@2 eq : {self._AA(th_list, aa_list, 2)}")
        print(f"AA@10 eq : {self._AA(th_list, aa_list, 10)}")
        print(f"AA@20 eq : {self._AA(th_list, aa_list, 20)}")
        plt.legend()
        plt.show()

    def _AA(self, x, y, threshold):
        """
        x : degree 전체를 모아 놓은 것(오름차순) => degree는 gt_vector, pred_vector 사이각
        y :   y = (1 + np.arange(len(err))) / len(loader) / n
            n : vpts 수  => 소실점의 수(데이터 수랑 같을 것 같은데?)
            len(loader) => validation 데이터(이미지)의 수(데이터 전체에 대해 10%~20%)
        """
        x = np.sort(x)

        index = np.searchsorted(x, threshold) # searchsorted : x[i-1] < threshold <= x[i] 조건을 만족하는 i를 구하는 함수
        x = np.concatenate([x[:index], [threshold]])
        y = np.concatenate([y[:index], [threshold]])
        return ((x[1:] - x[:-1]) * y[:-1]).sum() / threshold*100

    def __read_data(self, idx):
        gt_filename = self.gt_files[idx]
        result_filename = self.result_files[idx]
        # print(result_filename)
        gt_pt = self.__read_gt(gt_filename)
        result_pt = self.__read_result(result_filename)
        return gt_pt, result_pt

    def __read_gt(self,gt_filename):
        gt_filename = os.path.join(self.gt_root,gt_filename)
        if self.gt_format=='.npz':
            gt = np.load(gt_filename)
            gt = gt['vpts']
            # gt = self.gt3points(gt)
        return gt

    def __read_result(self, result_filename):
        # result는 전부 txt 일 예정
        result_filename = os.path.join(self.result_root, result_filename)
        with open(result_filename, 'r') as f:
            lines = f.readlines()
            lines = lines[0].strip().split(',')
            pred_x, pred_y = float(lines[5]), float(lines[6])
        return [pred_x, pred_y]
        
    def __compare_degree(self, gt, result, focal_length=2.1875*256, img_w_h=[512,512]):
        result = [result[0]-img_w_h[0]//2,result[1]-img_w_h[1]//2,focal_length]
        final_degree = 180
        final_gt = []

        for g in gt:
            degree, gt, result = self.get_degree(g, result, img_w_h)
            if degree<final_degree:
                final_gt = g
                final_degree = degree
        return final_degree, final_gt

    def check_img(self, idx, gt_pt, result_pt, degree):
        gt_x, gt_y = self.to_pixel(gt_pt) # FIXME : 입력 gt_pt 조정 필요
        img = cv2.imread(self.gt_img_files[idx])
        img = cv2.circle(img, (int(result_pt[0]), int(result_pt[1])), 5,(0,0,255),3)
        img = cv2.circle(img, (int(gt_x), int(gt_y)), 5,(0,255,0),3)
        
        text1 = f"pred {int(result_pt[0])}, {int(result_pt[1])}"
        text2 = f"gt {int(gt_x)}, {int(gt_y)}"
        text3 = f"deg {np.round(degree,2)}"
        cv2.putText(img, text1, (10,30), cv2.FONT_ITALIC, 1, (255,255,255), 2)
        cv2.putText(img, text2, (10,70), cv2.FONT_ITALIC, 1, (255,255,255), 2)
        cv2.putText(img, text3, (10,110), cv2.FONT_ITALIC, 1, (0,0,255), 2)
        

        cv2.imshow("image",img)
        cv2.waitKey(-1)
        cv2.destroyAllWindows()

    # # ========================= utils에 뺄까? ==============================
    def gt3points(self, vpts, focal_length=2.1875, h=512, w=512): # 기존 h=480, w=640
        x = vpts[:,0] / vpts[:, 2] * focal_length * max(h, w)/2.0 + w//2
        y = -vpts[:,1] / vpts[:, 2] * focal_length * max(h, w)/2.0 + h//2
        return x, y

    def to_pixel(self, vecs, focal_length=2.1875*256 , w=512):
        x = vecs[0] / vecs[2] * focal_length + w//2
        y = -vecs[1] / vecs[2] * focal_length + w//2
        return x, y
    
    def get_degree(self, gt, result, img_w_h):
        img_w_h = np.array(img_w_h)
        if gt[2]<0:
            gt[2] = -gt[2]
        gt = [gt[0],-(gt[1]),gt[2]]

        vp_norm = np.linalg.norm(result)
        gt_norm = np.linalg.norm(gt)

        dot_gt_vp = (np.array(gt) @ np.array(result))/(vp_norm*gt_norm) # .clip(max=1)
        degree = np.arccos(dot_gt_vp)*180/np.pi # neurvps 에서는 err로 되어있는 변수
        return degree, gt, result

    def vector_normalize(self, point_x, point_y, wh):
        cx = wh[0]//2
        cy = wh[1]//2
        f = 2.1875 * wh[0]//2
        vector = [(point_x-cx), (point_y-cy), f]
        # norm = np.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+f*f)
        return vector#/norm


def main():
    """
    su3 gt 파일을 받아서 계산하는 것을 구할 것

    road theta 결과와 su3 npz 파일을 비교하는 코드

    

    """
    ground_truth_root = "Y:/git/DeepGuider/bin/data/su3"
    result_root = "Y:/git/data_txt/result_su3_sample_new"
    # result_root = "C:/git/DeepGuider/bin/result_su3_sample_0528"
    # result_root = "Y:/git/data_txt/result_su3"

    su3 = Su3(ground_truth_root,result_root)
    su3.process_total_data()
    su3.process_total_result()

    # su3.summary()

if __name__=="__main__":
    main()