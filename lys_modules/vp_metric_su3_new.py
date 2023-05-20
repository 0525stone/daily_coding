"""
AA 그리는 것도 염두해둬야함
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

        self.gt_format = '.npz' # '.json'

        self.init_data()

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
            gt_filename = f"{self.gt_root}/{f_dir}/{fname}{self.gt_format}"
            self.gt_files.append(gt_filename)
                
    def loop_files(self):
        for idx, gt, result in enumerate(zip(self.gt_files, self.result_files)):
            assert gt!=result, f"{gt}\t{result}"
            self.check_degree(idx)
    
    def check_degree(self, idx):
        pass

    def check_img(self):
        pass





def main():
    """
    su3 gt 파일을 받아서 계산하는 것을 구할 것

    road theta 결과와 su3 npz 파일을 비교하는 코드

    

    """
    ground_truth_root = "Y:/git/DeepGuider/bin/data/su3"
    result_root = "Y:/git/data_txt/result_su3_sample_new"

    su3 = Su3(ground_truth_root,result_root)
    su3.summary()

if __name__=="__main__":
    main()