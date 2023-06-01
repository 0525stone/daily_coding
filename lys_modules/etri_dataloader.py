import os
import cv2

# from tqdm import tqdm
import math
import numpy as np
import matplotlib.pyplot as plt
"""
230528 현재
- TODO 어쨋거나 다른 알고리즘 적용하기 위해서는 frame 추출이 필요
- 현재는 txt 읽어서 하는 것 찾는 중..
"""


class ETRI_dataloader():
    def __init__(self, ground_truth_root, gt_txt, result_txt):
        self.gt_root = ground_truth_root # TODO : 데이터에 대한 객체를 만들어야하나?
        self.gt_txt = gt_txt
        self.result_txt = result_txt

        # 필요 파라미터들
        self.gt_format = '.npz' # '.json' TODO : json에 대해서도 읽을 수 있게 해야함ㄴ
        self.gt_img_format = '.png'
        self.img_ok = False # False True
        self.data_gt, self.data_res = self.init_data()

        self.degree_list = []

    def init_data(self):
        # TODO :read_data로 바꾸고 txt 를 읽은 것을 반환해주는 함수로 바꾸는 것이 나을 듯(재활용성)
        with open(self.gt_txt, 'r') as f:
            data_gt = self.gt = f.readlines()
        with open(self.result_txt, 'r') as results:
            data_res = results.readlines()
        return data_gt, data_res
    
    def summary(self):
        print(f"Ground truth root : {len(self.data_gt)}")
        print(f"result root : {len(self.data_res)}")
        print()
        
    def process_total_data(self, focal_length=1280):
        # MEMO : gt 에서 frame 숫자를 읽어서 result의 index로 읽어오기
        for idx, gt_line in enumerate(self.data_gt):
            # if idx<10:
            idx_data = int(gt_line.split(',')[0])
            print(f"\n{idx_data}\t{self.data_res[idx_data]}\n{gt_line}\n")
            gt_pt  = [float(gt_line.split(',')[2]), float(gt_line.split(',')[3]), focal_length]
            result_pt = self.__read_result_idx(self.data_res[idx_data], focal_length)
            degree, gt_pt, result_pt = self.process_data(gt_pt, result_pt)
            self.degree_list.append(degree)
        return self.degree_list

    def __read_result_idx(self, result_line, focal_length=640):
        result_pt = [float(result_line.split(',')[5]),float(result_line.split(',')[6]), focal_length]
        return result_pt

    def __compare_degree(self, gt, result, focal_length=640, img_w_h=[1280,720]):
        degree, gt, result = self.get_degree(gt, result, img_w_h)
        return degree, gt
   
    # =================================================================================
    # MEMO : vp_metric_su3_new에서 복붙하는 코드
    def process_data(self, gt_pt, result_pt):
        # 이 함수만 따로 쓸 수 있게 인자를 줘서 실행하게끔.. 전역변수로 프로그램 실행하는 것은 안좋dma
        degree, gt = self.__compare_degree(gt_pt, result_pt)
        # print(f"gt : {gt}\tpred : {result_pt}\ndegree : {degree}\n")
        return degree, gt, result_pt
    
    
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

if __name__ == "__main__":
    ground_truth_root = ""
    gt_txt = "Y:/git/data_txt/result_roadtheta/etri_cart_200219_15h01m_2fps_gt2.txt"
    result_txt = "Y:/git/data_txt/result_roadtheta/roadtheta_230601_222812.txt"
    etri = ETRI_dataloader(ground_truth_root, gt_txt, result_txt)
    etri.summary()
    etri.process_total_data()
    etri.process_total_result()

