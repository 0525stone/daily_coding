import os
import cv2

# from tqdm import tqdm
import math
import numpy as np
import matplotlib.pyplot as plt

class dataset_su3():
    """
    기본적으로 gt_dir에 라벨 파일 뿐만 아니라 png 파일까지 다 존재해야함..
    
    """
    def __init__(self, gt_dir="", pred_dir=""):
        self.gt_dir = gt_dir
        self.pred_dir = pred_dir
        self.gt_img = []
        self.gt_npz = []    # label 관련하여 논란이 많음.. json, npz, txt 세 종류가 있음...
        self.gt_json = []    
        self.pred_labels = []

    def read_files(self):
        gt_files = os.listdir(self.gt_dir)
        if "*.png" in gt_files:
            self.gt_img = [f for f in gt_files if "*.png" in f]
        if "*.npz" in gt_files:
            self.gt_npz = [f for f in gt_files if "*.npz" in f]
        if "*.json" in gt_files:
            self.gt_json = [f for f in gt_files if "*.json" in f]

        self.pred_labels = os.listdir(self.pred_dir)
        self.pred_labels = [f for f in self.pred_labels if "*.txt" in f]


def main():

    disk_dir = "/Users/johnlee" # "/Users/johnlee" ,"J:/"
    gt_dir = f"{disk_dir}/"
    pred_dir = f"{disk_dir}/"
    su3_vp = dataset_su3()


if __name__=="__main__":
    main()