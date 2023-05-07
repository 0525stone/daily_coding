"""
vp_performance 를 정리, 클래스화

extract_npz 로 나온 각 su3 상황에 맞는 gt를 갖고 결과 확인
"""
import os
import cv2

# from tqdm import tqdm
import math
import numpy as np
import matplotlib.pyplot as plt

class vp_metric_su3():
    def __init__(self, gt_paths, result_paths):
        self.f = 10
        self.gt_paths = gt_paths
        self.result_paths = result_paths
        self.AA_upper_th = 20000 # 20.000 degree
        self.AA_upper_th_lower = 1000

        # AA 구하기 위해
        self.err_list = []
    
    def vector_normalize(self, point_x, point_y, wh):
        cx = wh[0]/2
        cy = wh[1]/2
        f = 2.1875 * 256 # w[0]/2
        vector = [(point_x-cx), (point_y-cy), f]
        # norm = np.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+f*f)
        return vector#/norm

    # def find_vp(self, gt1, gt2):
    #     assert len(gt1)==4, f"gt1 has less than 4 components({len(gt1)})"
    #     gt1 = [int(i) for i in gt1]
    #     gt2 = [int(i) for i in gt2]
    #     a1 = gt1[3]-gt1[1]
    #     b1 = gt1[0]-gt1[2]
    #     c1 = gt1[1]*(gt1[2]-gt1[0])-gt1[0]*(gt1[3]-gt1[1])
    #     a2 = gt2[3]-gt2[1]
    #     b2 = gt2[0]-gt2[2]
    #     c2 = gt2[1]*(gt2[2]-gt2[0])-gt2[0]*(gt2[3]-gt2[1])

    #     vp_x = (c2*b1-c1*b2)/(a1*b2-a2*b1)
    #     vp_y = (a1*c2-a2*c1)/(a2*b1-a1*b2)

    #     return vp_x, vp_y

    def get_degree(self, gt_vp_x, gt_vp_y, pred_vp_x, pred_vp_y, wh):
        # print(f"To get AA in width {w}\ngt\t{gt_vp_x},{gt_vp_y}\nresult\t{pred_vp_x},{pred_vp_y}")
        wh = np.array(wh)
        vector_vp = self.vector_normalize(pred_vp_x, pred_vp_y, wh)
        vector_gt = self.vector_normalize(gt_vp_x, gt_vp_y, wh)
        vp_norm = np.linalg.norm(vector_vp)
        gt_norm = np.linalg.norm(vector_gt)

        dot_gt_vp = (np.array(vector_vp) @ np.array(vector_gt))/(vp_norm*gt_norm) # .clip(max=1)
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

    def AA_graph(self, err_list, ):
        assert len(err_list)==len(self.result_paths), f"different size  {len(err_list)}  {len(self.result_paths)}"
        for i, err in enumerate(err_list):
            aa_list = []
            th_list = []
            labelname = os.path.basename(self.result_paths[i])
            
            for th in range(0,self.AA_upper_th,1):
                th = th/self.AA_upper_th_lower

                for idx, e in enumerate(err):
                    if e<th: # err 를 정렬하였기 때문에, 
                        aa = (len(err)-idx+1)/len(err)
                        th_list.append(th)
                        aa_list.append(aa)
                        break
            plt.plot(th_list, aa_list, label=labelname)
            # print(f"{result_paths[i]}")
            print(f"AA@1 eq : {self.AA(th_list, aa_list, 1)}")
            print(f"AA@2 eq : {self.AA(th_list, aa_list, 2)}")
            print(f"AA@10 eq : {self.AA(th_list, aa_list, 10)}")
        plt.legend()
        plt.show()

    def result_summary(self):
        # gt_files = os.listdir(self.gt_path)
        # gt_files = sorted([f for f in gt_files if f.endswith(".txt")])

        print(len(self.gt_paths))
        for _,(gt_path, result_path) in enumerate(zip(self.gt_paths,self.result_paths)):
            gt_files = sorted(os.listdir(gt_path))
            result_files = sorted(os.listdir(result_path))

            aa_threshold = 6

            # f_save = open('data/result.txt','w')
            # f_save.write(f"filename,gt_x,gt_y,pred_x,pred_y,degree\n")

            score = []
            total = 0
            good = 0
            bad = 0
            err = []
            for idx, (gt_filename, result_filename) in enumerate(zip(gt_files, result_files)):
                # if idx<5:
                total+=1
                with open(os.path.join(gt_path, gt_filename), 'r') as f_gt:
                    with open(os.path.join(result_path, result_filename)) as f_result:
                        gt_line = f_gt.readlines()

                        if len(gt_line)==1:
                            # print(os.path.join(gt_path, gt_filename))
                            gt = gt_line[0].strip().split('\t')
                            gt = [float(p) for p in gt]
                            gt_x, gt_y = gt
                            # print(f"gt x,y {gt_x} {gt_y}")
                            # assert 0, "gt line"
                        
                            # 읽어들인 result에서 값 추출
                            result_line = f_result.readlines()
                            result_line = result_line[0].strip().split(',')
                            pred_vp_x, pred_vp_y = float(result_line[5]), float(result_line[6])
                            # print(f"vp_x, vp_y {gt_vp_x}, {gt_vp_y}\tresult : {pred_vp_x}, {pred_vp_y}")

                            # TODO : gt_vp_x, gt_vp_y, pred_vp_x, pred_vp_y 이렇게 네개로 누적 점수를 구하는 것이지
                            aa_degree = self.get_degree(gt_x, gt_y, pred_vp_x, pred_vp_y, [512,512])
                            err.append(aa_degree)
                            if aa_degree<aa_threshold:
                                good += 1
                            else:
                                bad += 1
                            score.append(aa_degree)
                            
                        else:   # 혹시 모를 상황
                            assert 0, f"need to check gt file name: {len(gt_line)} {gt_filename}"
                            # continue # TODO : continue를 하더라도 어떤 것을 패스했는지는 알아야하니 변수하나에 담아야함
                    
                # else:
                #     break
            err = -np.sort(-np.array(err))
            self.err_list.append(err)
            # f_save.close()
            # err = -np.sort(-np.array(err))
            # self.err_list.append(err)
            # print(f"err_list {len(self.err_list)}  {self.gt_paths}  {len(self.err_list[0])}")

        y = (1 + np.arange(len(err))) / total# / total # len(loader) / n => 각각 을 len(loader), n 으로 
        self.AA_graph(self.err_list, y)
            
        

if __name__=="__main__":

    root_dir = "/Users/johnlee"  # "J:/"
    su3_gt_dirs = [
                    # "J:/git/data_txt/gt_su3_val_f", 
                #   "J:/git/data_txt/gt_su3_val_f_vy_false",
                #   "J:/git/data_txt/gt_su3_vy_false",
                    # "J:/git/data_txt/gt_exp1",
                    # "J:/git/data_txt/gt_exp2",
                    # "J:/git/data_txt/gt_exp3",
                    "J:/git/data_txt/gt_su3_sample_new",
                    ]
    su3_preds_dirs = [
                        # "J:/git/data_txt/result_su3_val_f", 
                    #   "J:/git/data_txt/result_su3_val_f_vy_false",
                    #   "J:/git/data_txt/result_su3_vy_false",
                    #   "J:/git/data_txt/result_exp1_su3",
                    #   "J:/git/data_txt/result_exp2_su3",
                    #   "J:/git/data_txt/result_exp3_su3",
                      "J:/git/data_txt/result_su3_sample_new",                      
                      ]

    VP = vp_metric_su3(su3_gt_dirs, su3_preds_dirs)
    VP.result_summary()
    