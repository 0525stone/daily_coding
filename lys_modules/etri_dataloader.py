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
    def __init__(self, ground_truth_root, result_root, result_txt):
        self.gt_root = ground_truth_root # TODO : 데이터에 대한 객체를 만들어야하나?
        self.result_root = result_root

        # 필요 파라미터들
        self.gt_format = '.npz' # '.json' TODO : json에 대해서도 읽을 수 있게 해야함ㄴ
        self.gt_img_format = '.png'
        self.img_ok = False # False True



if __name__ == "__main__":
    ground_truth_root = ""
    result_root = ""
    pred_txt = "Y:/git/data_txt/roadtheta_230429_105343.txt"
    ETRI_dataloader(ground_truth_root, result_root, pred_txt)
