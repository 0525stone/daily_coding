import os
import cv2
import numpy as np

def to_pixel(vecs):
    x = vecs[0] / vecs[2] * (2.1875 * 256) + 256
    y = -vecs[1] / vecs[2] * (2.1875 * 256) + 256
    return x, y

def dot_product(vec1, vec2):
    dot_ = 0
    for v1, v2 in zip(vec1, vec2):
        dot_ += v1*v2
    result_dot = np.dot(vec1, vec2)

    return result_dot

def get_degree(vec1, vec2):
    vp_norm = np.linalg.norm(vec1)
    json_norm = np.linalg.norm(vec2)
    vp_json = dot_product(vec1, vec2)/vp_norm/json_norm

    degree = np.arccos(vp_json)
    return degree*180/np.pi



img_dir = "Y:/git/DeepGuider/bin/data/su3/000/0017_0.png"
vp = [136, 275, 2.1875 * 256]
json_data = [[ 0.97606232, -0.00642975,  0.21739599], 
         [-0.21749105, -0.02885559,  0.97563569],
         [0.        , 0.99956291, 0.02956327]]

img_dir = "Y:/git/DeepGuider/bin/data/su3/000/0022_0.png"
vp = [231, 246, 2.1875 * 256]
json_data = [([-0.05008141,  0.01662795,  0.99860671]), 
             ([9.98745139e-01, 8.33797578e-04, 5.00744691e-02]), 
             ([-0.        , -0.9998614 ,  0.01664884])]



img = cv2.imread(img_dir)
img = cv2.circle(img, (vp[0], vp[1]), 5,(0,0,255),3)


# x, y = to_pixel(json_data)
# json_xy = [x,y]

for gt in json_data:
    x,y = to_pixel(gt)
    print(f'gt x, y {x} {y}')
    img = cv2.circle(img, (int(x), int(y)), 5, (255,0,0),3)
    # dot_prod = dot_product(vp,d)
    degree = get_degree(vp,gt)
    print(f"degree : {degree}")

filename = os.path.basename(img_dir)
savename = f"result_{img_dir.split('/')[-2]}_{filename}"
cv2.imwrite(savename,img)
cv2.imshow("image",img)
cv2.waitKey(-1)
cv2.destroyAllWindows()