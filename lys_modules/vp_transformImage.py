import os
import cv2



def main():
    # 1. read file list
    root_dir = "../data/VP_image"
    dst_dir = "../data/VP_image_resized"
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        
    list_file = os.listdir(root_dir)

    # 2. read each file
    target_resized = 512

    for idx, filename in enumerate(list_file):
        #if idx < 5:
        file_dir = os.path.join(root_dir, filename)
        save_dir = os.path.join(dst_dir, filename)
        img_origin = cv2.imread(file_dir)
        if (len(img_origin.shape) == 3):
            height_img, width_img, channel_img = img_origin.shape
        elif (len(img_origin.shape) == 2):
            height_img, width_img = img_origin.shape
            channel_img = 1
        print(f"{file_dir}\nimg size : {img_origin.shape}")

        # 3. resize and padding
        if (height_img > width_img):
            width_resized = (int)(width_img / height_img * target_resized)
            height_resized = target_resized
            img_resized = cv2.resize(img_origin, (width_resized, height_resized))
        else:
            width_resized = target_resized
            height_resized = (int)(height_img / width_img * target_resized)
            img_resized = cv2.resize(img_origin, (width_resized, height_resized))
    
        cv2.imwrite(save_dir, img_resized)

if __name__ == "__main__":
    main()
