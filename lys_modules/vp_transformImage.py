import os
import cv2

import numpy as np

def main():
    # 1. read file list
    root_dir = "../data/VP_image"
    dst_dir = "../data/VP_image_resized"
    dst_dir_padding = "../data/VP_image_padding"
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    if not os.path.exists(dst_dir_padding):
        os.makedirs(dst_dir_padding)
        
    list_file = os.listdir(root_dir)

    # 2. read each file
    target_resized = 512

    for idx, filename in enumerate(list_file):
        #if idx < 5:
        file_dir = os.path.join(root_dir, filename)
        save_dir = os.path.join(dst_dir, filename)
        save_dir_padding = os.path.join(dst_dir_padding, filename)
        img_origin = cv2.imread(file_dir)
        if (len(img_origin.shape) == 3):
            height_img, width_img, channel_img = img_origin.shape
        elif (len(img_origin.shape) == 2):
            height_img, width_img = img_origin.shape
            channel_img = 1
        print(f"{file_dir}\nimg size : {img_origin.shape}")

        # 3. resize and padding
        img_padding = np.zeros(shape = (target_resized, target_resized, channel_img))

        if (height_img > width_img):
            width_resized = (int)(width_img / height_img * target_resized)
            height_resized = target_resized
            img_resized = cv2.resize(img_origin, (width_resized, height_resized))
            # insert resized image to padding image
            margin_padding = (int)((target_resized - width_resized)/2)
            img_padding[:, margin_padding:margin_padding+width_resized, :] = img_resized
        else:
            width_resized = target_resized
            height_resized = (int)(height_img / width_img * target_resized)
            img_resized = cv2.resize(img_origin, (width_resized, height_resized))
            margin_padding = (int)((target_resized - height_resized)/2)
            img_padding[margin_padding:margin_padding + height_resized, :, :] = img_resized
    
        
        cv2.imwrite(save_dir, img_resized)
        cv2.imwrite(save_dir_padding, img_padding)

if __name__ == "__main__":
    main()
