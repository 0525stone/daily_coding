import os
import numpy as np
import pandas as pd



def vp_check(list_file, root_dir):
    list_npz_file = [f for f in list_file if f.endswith("npz")]
    print(f"the number of npz files : {len(list_npz_file)}")

    width_image = 1280
    height_image = 720
    
    with open ("result_neurvps.txt", "w") as f_neurvps:
        string_result = f"{width_image}\t{height_image}"

        for idx, file in enumerate(list_file):
            # if idx < 10:
            file_dir = os.path.join(root_dir, file)
            with open(file_dir, 'r') as f:
                npz_data = np.load(file_dir)

                for vp in npz_data['vpts_pd']:
                    center_x_img = width_image/2
                    center_y_img = height_image/2

                    # 1. homogeneous coordinate to normal coordinate
                    x_homogeneous = vp[0]
                    y_homogeneous = vp[1]
                    z_homogeneous = vp[2]

                    if z_homogeneous == 0:
                        z_homogeneous = 0.001

                    x_normal = x_homogeneous/z_homogeneous
                    y_normal = y_homogeneous/z_homogeneous

                    # 2. normal coordinate to image coordinate
                    x_image = x_normal * center_x_img + center_x_img
                    y_image = y_normal * center_y_img + center_y_img
                    
                    x_image = round(x_image, 4)
                    y_image = round(y_image, 4)

                    # 3. check if vp is within image
                    if ((x_image <= width_image) & (x_image >= 0) & (y_image < height_image) & (y_image >= 0)):
                        print(f"{idx} th vp : {x_image} , {y_image}")
                        string_result = f"{string_result}\n{idx}\t{x_image}\t{y_image}"
        f_neurvps.write(string_result)
                






def main():
    # neurvps 결과 파일 dir
    file_dir = "./data/result_neurvps"
    list_file = os.listdir(file_dir)

    vp_check(list_file, file_dir)


if __name__=="__main__":
    main()