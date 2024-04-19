import os
import cv2

# from tqdm import tqdm
import math
import numpy as np
import matplotlib.pyplot as plt


"""
su3 데이터를 gt 파일 형식에서 읽어서 확인하는 부분
- gt는 gt 경로
- prediction 은 roadtheta 출력 형식으로
"""

class dataset_su3():
    def __init__(self):
        self.gt_dir = ""