import os
import cv2

import math
import numpy as np
import matplotlib.pyplot as plt

def vector_normalize(point_x, point_y, w):
    cx = w[0]/2
    cy = w[1]/2
    f = w[0]/2
    vector = [(point_x-cx)/f, (point_y-cy)/f, 1]
    norm = np.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+1)
    return vector/norm

def find_vp(gt1, gt2):
    assert len(gt1)==4, f"gt1 has less than 4 components({len(gt1)})"
    gt1 = [int(i) for i in gt1]
    gt2 = [int(i) for i in gt2]
    a1 = gt1[3]-gt1[1]
    b1 = gt1[0]-gt1[2]
    c1 = gt1[1]*(gt1[2]-gt1[0])-gt1[0]*(gt1[3]-gt1[1])
    a2 = gt2[3]-gt2[1]
    b2 = gt2[0]-gt2[2]
    c2 = gt2[1]*(gt2[2]-gt2[0])-gt2[0]*(gt2[3]-gt2[1])

    vp_x = (c2*b1-c1*b2)/(a1*b2-a2*b1)
    vp_y = (a1*c2-a2*c1)/(a2*b1-a1*b2)

    return vp_x, vp_y

def get_degree(gt_vp_x, gt_vp_y, pred_vp_x, pred_vp_y, w):
    # print(f"To get AA in width {w}\ngt\t{gt_vp_x},{gt_vp_y}\nresult\t{pred_vp_x},{pred_vp_y}")
    w = np.array(w)
    vector_vp = vector_normalize(pred_vp_x, pred_vp_y, w)
    vector_gt = vector_normalize(gt_vp_x, gt_vp_y, w)

    dot_gt_vp = (np.array(vector_vp) @ np.array(vector_gt)) # .clip(max=1)
    degree = np.arccos(dot_gt_vp)*180/np.pi # neurvps 에서는 err로 되어있는 변수
    return degree

def AA(x, y, threshold):
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

