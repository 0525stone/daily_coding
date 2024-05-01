import os 
import json
import numpy as np
import pandas as pd


def readlines_txt_files(file_dir):
    with open(file_dir, "r") as f:
        lines = f.readlines()

    return lines

def eda_gt(gt_lines):
    df_gt_column = []
    for idx, line in enumerate(gt_lines):
        if idx<10:
            words = line.split(",")
            if idx==0:
                start_idx = int(words[0])
                print(f"gt starting index : {start_idx}")
                for i in range(start_idx-1):
                    df_gt_column.append([0,0])
            else:
                df_gt_column.append([(float)(words[2]),(float)(words[3])])
    return df_gt_column

def compare_gt_2points(gt_point, point1, point2):

    distance1 = (gt_point[0] - point1[0])*(gt_point[0] - point1[0]) + (gt_point[1] - point1[1])*(gt_point[1] - point1[1])
    distance2 = (gt_point[0] - point2[0])*(gt_point[0] - point2[0]) + (gt_point[1] - point2[1])*(gt_point[1] - point2[1])

    if distance1 > distance2:
        return point2
    else:
        return point1

def eda_neurvps_vpestimation(result_lines, df_gt_column):
    df_result_column = []
    N_data = len(df_gt_column)
    former_idx = -1  # 중복의 점들을 처리하는 변수

    for idx, line in enumerate(result_lines):
        # if idx<10:
        words = line.split("\t")
        if len(words) <3:
            continue
        data_idx = int(words[0])
        vp_x = float(words[1])
        vp_y = float(words[2])

        if former_idx != data_idx:
            former_idx = data_idx
            df_result_column.append([vp_x, vp_y])
        else:
            # compare points with gt points
            new_point = compare_gt_2points(df_gt_column[former_idx], df_result_column[former_idx], [vp_x, vp_y])
            df_result_column[former_idx] = new_point

        if data_idx==N_data-1:
            break
    return df_result_column

def eda_roadtheta(roa_lines, df_gt_column):
    df_roadtheta_column = []
    N_data = len(df_gt_column)

    for idx, line in enumerate(roa_lines):
        words = line.split(",")
        pass

def main():
    root_dir = "./data/etri_dataset"
    gt_dir = "etri_cart_200219_15h01m_2fps_gt3.txt"
    neurvps_dir = "result_neurvps.txt"
    vpestimation_dir = "result_vpestimation.txt"
    roadtheta_dir = "result_roadtheta.txt"

    gt_dir = os.path.join(root_dir, gt_dir)
    neurvps_dir = os.path.join(root_dir, neurvps_dir)
    vpestimation_dir = os.path.join(root_dir, vpestimation_dir)
    roadtheta_dir = os.path.join(root_dir, roadtheta_dir)

    gt_lines = readlines_txt_files(gt_dir)
    neu_lines = readlines_txt_files(neurvps_dir)
    vpe_lines = readlines_txt_files(vpestimation_dir)
    roa_lines = readlines_txt_files(roadtheta_dir)

    print(f"gt lines : {len(gt_lines)}\n{gt_lines[0]}")
    print(f"neurvps lines : {len(neu_lines)}\n{neu_lines[0]}")
    print(f"vpestimation lines : {len(vpe_lines)}\n{vpe_lines[0]}")
    print(f"roadtheta lines : {len(roa_lines)}\n{roa_lines[0]}")

    # Dataframe 만듦기
    df_gt_column = eda_gt(gt_lines)
    df_neurvps_column = eda_neurvps_vpestimation(neu_lines, df_gt_column)
    df_vpestimation_column = eda_neurvps_vpestimation(vpe_lines, df_gt_column)
    df_roadtheta_column = eda_roadtheta(roa_lines, df_gt_column)

    print(f"gt_column : {len(df_gt_column)}\nneurvps_column : {len(df_neurvps_column)}\nvpestimation_column : {len(df_vpestimation_column)}")

if __name__ =="__main__":
    main()