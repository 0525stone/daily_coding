"""
각 결과 파일들을 읽어서 성능 계산

prefix로 각 파일에 대해 directory, prefix 설정하여 읽어오기
"""
import os
import cv2

def vp_performance(gt_path, result_path, gt_prefix="", result_prefix=""):
    """
    파일명을 오리지날 이미지파일 이름에서 긁어올지 결과 txt 파일로 할지 정해야함..
    """
    gt_files = os.listdir(gt_path)
    result_files = os.listdir(result_path)
    gt_files = sorted([f for f in gt_files if f.endswith(".txt")])
    result_files = sorted([f for f in result_files if f.endswith(".txt")])

    for gt, result in zip(gt_files, result_files):
        print(f"{gt}, {result}")
        with open(os.path.join(gt_path, gt), 'r') as f_gt:
            with open(os.path.join(result_path, result)) as f_result:
                print(f"{f_gt.readline()}")


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