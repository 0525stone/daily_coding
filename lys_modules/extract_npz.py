import os
import numpy as np
from vp_utils import vectorize, find_vp, get_degree, AA
from vp_metric_su3 import vp_metric

class su3_file():
    def __init__(self, filename):
        self.filename = filename
        self.contents = np.load(filename)
        vpts = self.contents['vpts']
        print(vpts)
        y,x = self.to_pixel(vpts, focal_length=2.1875)
        print(f"vpts 결과 {x}, {y}")
    def to_pixel(self, vpts, focal_length=1.0, h=512, w=512): # 기존 h=480, w=640
        x = vpts[:,0] / vpts[:, 2] * focal_length * max(h, w)/2.0 + w//2
        y = -vpts[:,1] / vpts[:, 2] * focal_length * max(h, w)/2.0 + h//2
        return y, x
    def to_pixel_neurvps(self, w, focal_length=2.1875):
        x = w[0] / w[2] * focal_length * 256 + 256
        y = -w[1] / w[2] * focal_length * 256 + 256
        return y, x
        
def npz2points(vpts, focal_length=1.0, h=512, w=512): # 기존 h=480, w=640
    x = vpts[:,0] / vpts[:, 2] * focal_length * max(h, w)/2.0 + w//2
    y = -vpts[:,1] / vpts[:, 2] * focal_length * max(h, w)/2.0 + h//2
    return y, x

# # npz2points 도 결국 같은 얘기를 하는 것임
# def to_pixel(w):
#     x = w[0] / w[2] * C.io.focal_length * 256 + 256
#     y = -w[1] / w[2] * C.io.focal_length * 256 + 256
#     return y, x


def get1point(x, y, pred_x, pred_y):
    """
    gt 3개와 pred 주면 제일 가까운 점 하나를 찾아줌
    """
    min_th = (pred_x-x[0])*(pred_x-x[0]) + ((pred_y-y[0]))*(pred_y-y[0])
    min_x = x[0]
    min_y = y[0]
    # TODO : 여기가 의심됨
    for temp_x,temp_y in zip(x, y):
        temp_th = (pred_x-temp_x)*(pred_x-temp_x) + ((pred_y-temp_y))*(pred_y-temp_y)
        if temp_th<min_th:
            min_x = temp_x
            min_y = temp_y
            min_th = temp_th
    return min_x, min_y

def extract_vp_su3(su3_gt_new_dirs, su3_preds_dirs, su3_root):
    # su3_root = "J:/git/DeepGuider/bin/data/gt_su3"
    gt_files = sorted(os.listdir(su3_root))
    for su3_gt_new_dir in su3_gt_new_dirs:
        if not os.path.exists(su3_gt_new_dir):
            os.mkdir(su3_gt_new_dir)
    for su3_preds_dir, su3_gt_new_dir in zip(su3_preds_dirs, su3_gt_new_dirs):
        pred_files = sorted(os.listdir(su3_preds_dir)) # TODO : gt_file을 보고 pred_file 이름을 알 수 있음
        # print(f"pred files {len(pred_files)}\n{pred_files[:5]}")

        for idx, (gt_file, pred_file) in enumerate(zip(gt_files, pred_files)):
            # if idx<5:
            filename = pred_file.split(".")[0]

            # gt 3개의 점 읽어옴
            gt_filename = os.path.join(su3_root,f"{filename}_label.npz")
            gt_content = np.load(gt_filename)
            vpts = gt_content['vpts']
            print(f"{gt_filename}\t{pred_file}")
            gt_y, gt_x = npz2points(vpts)

            # pred 1개의 점 읽어옴
            pred_filename = os.path.join(su3_preds_dir, pred_file)
            with open(pred_filename, 'r') as f:
                result_line = f.readlines()
                result_line = result_line[0].strip().split(',')
                pred_x, pred_y = float(result_line[5]), float(result_line[6])
            
            gt_x, gt_y = get1point(gt_x, gt_y, pred_x, pred_y)         
            save_filename = os.path.join(su3_gt_new_dir, pred_file)

            print(f"{save_filename}\npoints\n{gt_x}\t{gt_y}\n{pred_x}\t{pred_y}")
            with open(save_filename, 'w') as f_save:
                f_save.write(f"{gt_x}\t{gt_y}\n")


def main():
    # npz_filename = "data/0000_0_label.npz"
    # s = su3_file(npz_filename)

    root_dir =  "J:" # "/Users/johnlee" ,"J:/"
    su3_root = f"{root_dir}/git/DeepGuider/bin/data/gt_su3"
    # su3_root = f"{root_dir}/git/data_txt/su3_labels"
    gt_files = os.listdir(su3_root)
    print(f"files : {len(gt_files)}\n{gt_files[:5]}")

    su3_preds_dirs = [
                        # "J:/git/data_txt/result_su3_val_f", 
                    #   "J:/git/data_txt/result_su3_val_f_vy_false",
                    #   "J:/git/data_txt/result_su3_vy_false",
                    # f"{root_dir}/git/data_txt/result_exp1_su3",
                    # f"{root_dir}/git/data_txt/result_exp2_su3",
                    # f"{root_dir}/git/data_txt/result_exp3_su3",
                    f"{root_dir}/git/data_txt/result_su3_sample_new",
                      ]
    su3_gt_new_dirs = [
                        # "J:/git/data_txt/gt_su3_val_f", 
                    #   "J:/git/data_txt/gt_su3_val_f_vy_false",
                    #   "J:/git/data_txt/gt_su3_vy_false",
                    #   f"{root_dir}/git/data_txt/gt_exp1",
                    #   f"{root_dir}/git/data_txt/gt_exp2",
                    #   f"{root_dir}/git/data_txt/gt_exp3",
                    f"{root_dir}/git/data_txt/gt_su3_sample_new",
                      ]
    extract_vp_su3(su3_gt_new_dirs, su3_preds_dirs, su3_root)

    vp_check = vp_metric(su3_gt_new_dirs, su3_preds_dirs)
    vp_check.result_summary()


            # print(vpts)



if __name__=="__main__":
    main()