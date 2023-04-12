import os
import cv2

import math
import numpy as np
import matplotlib.pyplot as plt




class vp_evaluation():
    def __init__(self, gt_dir="data/gt", pred_dir="data/result"):
        self.gt_directory = gt_dir
        self.pred_directory = pred_dir
        self.threshold = 6

    def __init__data(self):
        # TODO : 디렉토리 구조에 따라서 다르게 읽어오게 할 필요가 있음
        self.gt_files = os.listdir(self.gt_directory)
        self.pred_files = os.listdir(self.pred_directory)
        self.gt_files = sorted([os.path.join(self.gt_directory,f) for f in gt_files if f.endswith(".txt")])
        self.pred_files = sorted([os.path.join(self.pred_directory,f) for f in pred_files if f.endswith(".txt")])

        self.get_degree_list()

    def get_degree_list(self):
        for gt_filename, pred_filename in zip(self.gt_files, self.pred_files):
            with open(gt_filename, 'r') as f_gt


    def save(self):
        pass
