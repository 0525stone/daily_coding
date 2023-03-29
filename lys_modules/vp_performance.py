"""
각 결과 파일들을 읽어서 성능 계산

prefix로 각 파일에 대해 directory, prefix 설정하여 읽어오기
"""
import os
import cv2

def find_vp_gt(gt1, gt2):
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


def vp_performance(gt_path, result_path, gt_prefix="", result_prefix=""):
    """
    파일명을 오리지날 이미지파일 이름에서 긁어올지 결과 txt 파일로 할지 정해야함..
    """
    gt_files = os.listdir(gt_path)
    result_files = os.listdir(result_path)
    gt_files = sorted([f for f in gt_files if f.endswith(".txt")])
    result_files = sorted([f for f in result_files if f.endswith(".txt")])

    for gt_filename, result_filename in zip(gt_files, result_files):
        print(f"{gt_filename}, {result_filename}")
        with open(os.path.join(gt_path, gt_filename), 'r') as f_gt:
            with open(os.path.join(result_path, result_filename)) as f_result:
                gt_line = f_gt.readlines()
                if len(gt_line)==3:
                    # 
                    gt1 = gt_line[1].replace('  ',' ').strip().split(' ')
                    gt2 = gt_line[2].replace('  ',' ').strip().split(' ')
                    gt1 = [float(i) for i in gt1]
                    gt2 = [float(i) for i in gt2]
                    print(f"{gt1}\t{type(gt1)}")
                    print(f"{gt2}\t{type(gt2)}")
                    vp_x, vp_y = find_vp_gt(gt1, gt2)  # TODO : vp_x, vp_y 검증 필요. 선이랑 점 다 그려보면 됨 => 손으로 그려봤는데 맞음
                    print(f"vp_x, vp_y {vp_x} {vp_y}")
                    assert len(gt1)==len(gt2), f"gt1 : {len(gt1)}   gt2 : {len(gt2)}"
                    
                else:   # 혹시 모를 상황
                    assert 0, f"need to check gt file name: {gt_filename}"
                    # continue # TODO : continue를 하더라도 어떤 것을 패스했는지는 알아야하니 변수하나에 담아야함
                # print(f"{f_result.readlines()}")  # [0]를 해야 text 접근 => split(",")  => [6, 7] 이 좌표인듯?
                print()
                
                


    print(f"gt files : {len(gt_files)}\nres files : {len(result_files)} ")

def main():
    print("VP performance code")
    gt_path="data/gt"
    result_path="data/result"
    vp_performance(gt_path, result_path,result_prefix="ava_")


if __name__=="__main__":
    main()
"""
참조한 링크들
- with open as f : https://starriet.medium.com/python-with-open-as-f-%EC%97%90%EC%84%9C-f%EC%9D%98-%EC%A0%95%EC%B2%B4%EB%8A%94-3cb48ea9e302

"""