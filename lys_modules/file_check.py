import os

def read_lines_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(f"lines from file : {len(lines)}")
    return lines

gt_filename = '../../bin/etri_cart_200219_15h01m_2fps_gt3.txt'
pred_filename = '../../bin/roadtheta_230409_200048.txt'

gt_lines = read_lines_file(gt_filename)
pred_lines = read_lines_file(pred_filename)

# last line check
print(f"gt last line : {gt_lines[-1]}")
print(f"pred last line : {pred_lines[-1]}")

"""
230408에 한 실험으로는 매칭이 안됨.. 아마 fps 설정이 15로 되어있어서 그런듯?
230409 20시에 다시 실험 진행중 => fps 2로

"""
for i, gt_line in enumerate(gt_lines):
    if i<40:
        gt_line = gt_line.strip()
        gt_line = gt_line.split(',')
        gt_line = [int(float(gt)) for gt in gt_line]
        idx = gt_line[0]
#         idx = int(gt_line.split(',')[0])
        pred_line = pred_lines[idx]
        pred_line = pred_line.split(',')
        pred_line = [int(float(pred)) for pred in pred_line[5:8]]
        print(f"{idx}\t{gt_line[2]}, {gt_line[3]}\t{pred_line}")
        
    