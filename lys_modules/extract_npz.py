import os
import numpy as np
from vp_utils import vectorize, find_vp, get_degree, AA

class su3_file():
    def __init__(self, filename):
        self.filename = filename
        self.contents = np.load(filename)
        vpts = self.contents['vpts']
        print(vpts)
        y,x = self.to_pixel(vpts)
        print(f"vpts 결과 {x}, {y}")
    def to_pixel(self, vpts, focal_length=1.0, h=512, w=512): # 기존 h=480, w=640
        x = vpts[:,0] / vpts[:, 2] * focal_length * max(h, w)/2.0 + w//2
        y = -vpts[:,1] / vpts[:, 2] * focal_length * max(h, w)/2.0 + h//2
        return y, x
    
def main():
    # npz_filename = "data/0000_0_label.npz"
    # s = su3_file(npz_filename)


    su3_root = "/Volumes/LYS/git/Deepguider/bin/data/gt_su3"
    gt_files = os.listdir(su3_root)
    print(f"files : {len(gt_files)}\n{gt_files[:5]}")

    su3_preds_dirs = ["/Users/johnlee/git/daily_coding/vp_data/result_su3_val_f", 
                      "/Users/johnlee/git/daily_coding/vp_data/result_su3_val_f_vy_false",
                      "/Users/johnlee/git/daily_coding/vp_data/result_su3_vy_false"
                      ]
    for su3_preds_dir in su3_preds_dirs:
        pred_files = sorted(os.listdir(su3_preds_dir))
        print(f"pred files {len(pred_files)}\n{pred_files[:5]}")

    for idx, (gt_file, pred_file) in enumerate(zip(gt_files, pred_files)):
        if idx<5:
            filename = gt_file.split(".")[0][:-6]
            print(f"{filename}\t{pred_file}")


if __name__=="__main__":
    main()