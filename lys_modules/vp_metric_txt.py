"""
vp_performance 를 정리, 클래스화

roadtheta 전용 utils 를 만들어서 txt 읽어들이고 점수 계산하는 코드들을 utils에 주면 좋을 듯
"""
import os
import cv2

import math
import numpy as np
import matplotlib.pyplot as plt

class vp_metric_txt():
    def __init__(self, file_txt, gt_path, result_paths):
        self.f = 10
        self.file_txt = file_txt
        with open(file_txt, 'r') as f:
            self.files = f.readlines()
            self.files = [file.strip() for file in self.files]
        self.gt_path = gt_path
        self.result_paths = result_paths
        self.AA_upper_th = 2000

        # AA 구하기 위해
        self.err_list = []

    def result_summary(self):
        score = []
        total = 0
        good = 0
        bad = 0
        err = []

        for filename in self.files:
            aa_threshold = 6
            filename = f"{filename.split('.')[0]}.txt"

            # f_save = open('data/result.txt','w')
            # f_save.write(f"filename,gt_x,gt_y,pred_x,pred_y,degree\n")


            total+=1
            with open(os.path.join(self.gt_path, filename), 'r') as f_gt:
                with open(os.path.join(result_paths, filename), 'r') as f_result:
                    gt_line = f_gt.readlines()
                    if len(gt_line)==3:
                        w = gt_line[0].strip().replace('  ',' ').split(' ')
                        w = [int(_) for _ in w]
                        
                        gt1 = gt_line[1].replace('  ',' ').replace('  ',' ').strip().split(' ')   # TODO : pseudo로 공백들에 대하여 수정해줌
                        gt2 = gt_line[2].replace('  ',' ').replace('  ',' ').strip().split(' ')
                        assert len(gt1)==len(gt2), f"gt1 : {len(gt1)}   gt2 : {len(gt2)}, \n{gt1}\n{gt2}\n{gt_line}"

                        gt1 = [float(i) for i in gt1]
                        gt2 = [float(i) for i in gt2]
                        gt_vp_x, gt_vp_y = self.find_vp(gt1, gt2)  # Done by 수기 : vp_x, vp_y 검증 필요. 선이랑 점 다 그려보면 됨 => 손으로 그려봤는데 맞음

                        # 읽어들인 result에서 값 추출
                        result_line = f_result.readlines()
                        result_line = result_line[0].strip().split(',')
                        pred_vp_x, pred_vp_y = float(result_line[5]), float(result_line[6])
                        # print(f"vp_x, vp_y {gt_vp_x}, {gt_vp_y}\tresult : {pred_vp_x}, {pred_vp_y}")

                        # TODO : gt_vp_x, gt_vp_y, pred_vp_x, pred_vp_y 이렇게 네개로 누적 점수를 구하는 것이지
                        aa_degree = self.get_degree(gt_vp_x, gt_vp_y, pred_vp_x, pred_vp_y, w)
                        err.append(aa_degree)
                        if aa_degree<aa_threshold:
                            good += 1
                        else:
                            bad += 1
                        score.append(aa_degree)
                        
                    else:   # 혹시 모를 상황
                        assert 0, f"need to check gt file name: {filename}"
                        # continue # TODO : continue를 하더라도 어떤 것을 패스했는지는 알아야하니 변수하나에 담아야함
            # f_save.close()
        err = -np.sort(-np.array(err))
        self.err_list.append(err)
        y = (1 + np.arange(len(err))) / total# / total # len(loader) / n => 각각 을 len(loader), n 으로 
        self.AA_graph(self.err_list, y)
        
    
    def vectorize(self, point_x, point_y, w):
        cx = w[0]/2
        cy = w[1]/2
        f = w[0]/2
        vector = [(point_x-cx)/f, (point_y-cy)/f, 1]
        norm = np.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+1)
        return vector/norm

    def find_vp(self, gt1, gt2):
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

    def get_degree(self, gt_vp_x, gt_vp_y, pred_vp_x, pred_vp_y, w):
        # print(f"To get AA in width {w}\ngt\t{gt_vp_x},{gt_vp_y}\nresult\t{pred_vp_x},{pred_vp_y}")
        w = np.array(w)
        vector_vp = self.vectorize(pred_vp_x, pred_vp_y, w)
        vector_gt = self.vectorize(gt_vp_x, gt_vp_y, w)

        dot_gt_vp = (np.array(vector_vp) @ np.array(vector_gt)) # .clip(max=1)
        degree = np.arccos(dot_gt_vp)*180/np.pi # neurvps 에서는 err로 되어있는 변수
        return degree

    def AA(self, x, y, threshold):
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

    def AA_graph(self, err_list, y):
        # assert len(err_list)==len(self.result_paths), f"different size\t{len(err_list)}\t{len(self.result_paths)}"
        for i, err in enumerate(err_list):
            aa_list = []
            th_list = []
            
            for th in range(0,self.AA_upper_th*10,1):
                th = th/1000
                for idx, e in enumerate(err):
                    if e<th: # err 를 정렬하였기 때문에, 
                        aa = (len(err)-idx+1)/len(err)
                        th_list.append(th)
                        aa_list.append(aa)
                        break
            plt.plot(th_list, aa_list, label=f"result_{i}")
            print(f"{result_paths[i]}")
            print(f"AA@1 eq : {self.AA(th_list, aa_list, 1)}")
            print(f"AA@2 eq : {self.AA(th_list, aa_list, 2)}")
            print(f"AA@10 eq : {self.AA(th_list, aa_list, 10)}")
        plt.legend()
        plt.show()

    

if __name__=="__main__":

    # root_dir = "J:/" # J:/   /Users/johnlee
    # dataset_name = "ava"
    # dataset_name = "flickr"
    # # dataset_name = "su3" 

    # if dataset_name=="ava":
    #     gt_path = "/Users/johnlee/git/daily_coding/vp_data/gt_ava" # "D:\git\data_txt/vp-labels/gt_ava"
    #     result_paths = [
    #                     "/Users/johnlee/git/daily_coding/vp_data/result_ava", 
    #                 "/Users/johnlee/git/daily_coding/vp_data/result_ava_geo_false_vy_false",
    #                 "/Users/johnlee/git/daily_coding/vp_data/result_ava_vy_false",
    #                 "/Users/johnlee/git/daily_coding/vp_data/result_ava_val_f_vy_false"
    #                 ]
    # elif dataset_name=="flickr":
    #     dir_root = "D:\git\data_txt"
    #     gt_path = f"{dir_root}/vp-labels/gt_ava"# "/Users/johnlee/git/daily_coding/vp_data/gt_flickr" # "D:\git\data_txt/vp-labels/gt_ava"
    #     result_paths = [
    #             "/Users/johnlee/git/daily_coding/vp_data/result_flickr", #"/Users/johnlee/git/daily_coding/vp_data/result_flickr", 
    #             "/Users/johnlee/git/daily_coding/vp_data/result_flickr_geo_false_vy_false",
    #             "/Users/johnlee/git/daily_coding/vp_data/result_filckr_vy_false",
    #                 "/Users/johnlee/git/daily_coding/vp_data/result_flickr_val_f_vy_false"
    #     ]
    dir_root = "J:/git/data_txt"
    file_txt = f"{dir_root}/gt_valid/valid.txt" # D:/git/DeepGuider/bin/data/tmm17/valid.txt
    gt_path = f"{dir_root}/gt_valid"
    result_paths = f"{dir_root}/result_valid1"
    
    VP = vp_metric_txt(file_txt, gt_path, result_paths)
    VP.result_summary()
    