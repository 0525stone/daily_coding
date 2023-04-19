"""
vp_performance 를 정리, 클래스화

"""
import os
import cv2

import math
import numpy as np
import matplotlib.pyplot as plt

class vp_metric():
    def __init__(self, gt_path, result_paths):
        self.f = 10
        self.gt_path = gt_path
        self.result_paths = result_paths
    
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
        x : degree 전체를 모아 놓은 것
        y :   y = (1 + np.arange(len(err))) / len(loader) / n
            n : vpts 수  => 소실점의 수(데이터 수랑 같을 것 같은데?)
            len(loader) => 데이터(이미지)의 수
        """
        # x = np.sort(x)[::-1]
        x = np.sort(x)

        index = np.searchsorted(x, threshold)
        x = np.concatenate([x[:index], [threshold]])
        y = np.concatenate([y[:index], [threshold]])
        return ((x[1:] - x[:-1]) * y[:-1]).sum() / threshold

    def AA_graph(self, x_list, y, threshold=200):
        # aa_list = []
        # th_list = []
        assert len(x_list)==len(self.result_paths), "different size"
        print(f"why?\t\t{len(x_list)}")
        for i, err in enumerate(x_list):
            aa_list = []
            th_list = []
            
            for th in range(0,threshold*10,1):
                th = th/100
                
                # print(f"threshold {th}")
                for idx, e in enumerate(err):
                    if e<th: # err 를 정렬하였기 때문에, 
                        # print(f"check\t{idx}\t{e} {th} {err[idx]}")
                        aa = (len(err)-idx+1)/len(err)
                        th_list.append(th)
                        aa_list.append(aa)
                        # print(f"aa accuracy : {idx} {aa}")
                        break
                if th in [1,2,10]:
                # if th in [0.1,0.2,1]:
                    print(f"{th} in threshold list")
                    y_AA = (1 + np.arange(len(err))) / len(err)/ len(err)#/ (0.2*len(err))#/ (0.2*len(err))# / len(err)
                    AA_value = self.AA(err, y_AA, th)
                    print(f"{th}\t{AA_value}")
            plt.plot(th_list, aa_list, label=f"result_{i}")
            value_aa = self.AA_area(th_list, aa_list, 0.1)
            print(f"0.1 area of AA : {value_aa}")
        # print(f"err {err[:10]}")

        plt.legend()
        plt.show()

    def AA_area(self, th_list, aa_list, th):
        area = 0
        for t,a in zip(th_list, aa_list):
            if t<=th:
                area+=a
        return area/th


    def getting_x_y(self):
        x_list = []
        gt_files = os.listdir(self.gt_path)
        gt_files = sorted([f for f in gt_files if f.endswith(".txt")])
        for result_path in self.result_paths:
            
            result_files = os.listdir(result_path)
            
            result_files = sorted([f for f in result_files if f.endswith(".txt")])
            aa_threshold = 6

            # f_save = open('data/result.txt','w')
            # f_save.write(f"filename,gt_x,gt_y,pred_x,pred_y,degree\n")

            score = []
            total = 0
            good = 0
            bad = 0
            err = []
            for gt_filename, result_filename in zip(gt_files, result_files):
                total+=1
                with open(os.path.join(self.gt_path, gt_filename), 'r') as f_gt:
                    with open(os.path.join(result_path, result_filename)) as f_result:
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
                                # print(f'aa degree : {aa_degree}')
                                # print(f"good case {aa_degree}", gt_vp_x, gt_vp_y, pred_vp_x, pred_vp_y)
                                good += 1
                            else:
                                # print(f"bad case {aa_degree}", gt_vp_x, gt_vp_y, pred_vp_x, pred_vp_y)
                                bad += 1
                            # f_save.write(f"{gt_filename},{gt_vp_x},{gt_vp_y},{pred_vp_x},{pred_vp_y},{aa_degree}\n")
                            score.append(aa_degree)
                            
                        else:   # 혹시 모를 상황
                            assert 0, f"need to check gt file name: {gt_filename}"
                            # continue # TODO : continue를 하더라도 어떤 것을 패스했는지는 알아야하니 변수하나에 담아야함
            # f_save.close()
            err = -np.sort(-np.array(err))
            x_list.append(err)
        y = (1 + np.arange(len(err))) / total# / total # len(loader) / n => 각각 을 len(loader), n 으로 
        print(f"{len(x_list)}")
        self.AA_graph(x_list, y)
        

if __name__=="__main__":
    gt_path = "D:\git\data_txt/vp-labels/AVA_landscape"
    result_paths = [
                    "D:\git\data_txt/result_ava", 
                #    "/Users/johnlee/git/daily_coding/vp_data/result_ava_geo_false_vy_false",
                #    "/Users/johnlee/git/daily_coding/vp_data/result_ava_vy_false"
                   ]
    VP = vp_metric(gt_path, result_paths)
    VP.getting_x_y()
    