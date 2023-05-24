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
        self.img_ok = False

        # points 정보들 들고 있어야하나?
        self.gt_pts = [] # 몇만개의 데이터에 대해서 갖고 있게끔 하는게 맞을까? 그때 그때 읽어서 하는게 나을듯
        self.result_pts = []

        self.init_data()
        # self.loop_files()

    def summary(self):
        print(f"Ground truth root : {self.gt_root} files : {len(self.gt_files)}")
        print(f"result root : {self.result_root} files : {len(self.result_files)}")
        print()

    def init_data(self):
        self.gt_files = []
        self.result_files = sorted(os.listdir(self.result_root))
        # gt 파일들은 경로를 불러오는데 방법이 필요함 => 결과 파일명에서 경로를 따로 따내서 해야함
        for idx, f in enumerate(self.result_files):
            # if idx<5:
            #     print(f)
            filename = os.path.basename(f)
            f_dir = filename.split('_')[0]
            fname = '_'.join(os.path.basename(f).split('_')[1:]).split('.')[0]
            if self.gt_format=='.npz':
                gt_filename = f"{self.gt_root}/{f_dir}/{fname}_label{self.gt_format}"
            elif self.gt_format=='.json': 
                gt_filename = f"{self.gt_root}/{f_dir}/{fname}_camera{self.gt_format}"
            self.gt_files.append(gt_filename)
                
    def loop_files(self):
        for idx, (gt, result) in enumerate(zip(self.gt_files, self.result_files)): # FIXME : gt, result없이 그냥 idx만 읽게 해도됨
            assert gt!=result, f"{gt}\t{result}"
            if idx<1:
                if self.img_ok:
                    self.check_img()
            # FIXME : 예외처리해야함. 파일 만약에 없는 경우...
                self.read_data(idx) # TODO : idx로 img를 불러오려면.. 
                

    def read_data(self, idx):
        gt_filename = self.gt_files[idx]
        result_filename = self.result_files[idx]
        print(result_filename)
        gt_pt = self.__read_gt(gt_filename)
        result_pt = self.__read_result(result_filename)
        degree = self.compare_degree(gt_pt, result_pt)

        if self.img_ok:
            gt_x, gt_y = self.to_pixel(gt_pt) # FIXME : 입력 gt_pt 조정 필요
            self.check_img()

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
        
    def compare_degree(self, gt, result, focal_length=2.1875*256):
        print(f"vp:{result}\ngt:{gt}")
        result = [result[0],result[1],focal_length]
        wh = [512,512]
        for g in gt:
            degree = self.get_degree(g, result, wh)
            print(f"result {degree} {g}")

        pass

    def check_img(self):
        pass

    # # ========================= utils에 뺄까? ==============================
    def gt3points(self, vpts, focal_length=2.1875, h=512, w=512): # 기존 h=480, w=640
        x = vpts[:,0] / vpts[:, 2] * focal_length * max(h, w)/2.0 + w//2
        y = -vpts[:,1] / vpts[:, 2] * focal_length * max(h, w)/2.0 + h//2
        return x, y

    def to_pixel(self, vecs, focal_length=2.1875*256 , w=512):
        x = vecs[0] / vecs[2] * focal_length + w//2
        y = -vecs[1] / vecs[2] * focal_length + w//2
        return x, y
    
    def get_degree(self, gt, result, wh):
        wh = np.array(wh)
        gt = [gt[0],-(gt[1]),gt[2]]
        result = [result[0]-wh[0]//2, result[1]-wh[1]//2, result[2]]

        vp_norm = np.linalg.norm(result)
        gt_norm = np.linalg.norm(gt)

        dot_gt_vp = (np.array(gt) @ np.array(result))/(vp_norm*gt_norm) # .clip(max=1)
        degree = np.arccos(dot_gt_vp)*180/np.pi # neurvps 에서는 err로 되어있는 변수
        return degree

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

    su3 = Su3(ground_truth_root,result_root)

    vp = [231, 246, 2.1875 * 256]
    gt = [([-0.05008141,  0.01662795,  0.99860671]), 
      ([9.98745139e-01, 8.33797578e-04, 5.00744691e-02]), 
      ([-0.        , -0.9998614 ,  0.01664884])]
    su3.compare_degree(gt, vp)
    su3.loop_files()
    # su3.summary()

if __name__=="__main__":
    main()