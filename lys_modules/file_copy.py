import os
import random
import shutil
from tqdm import tqdm

"""
트리구조 디렉토리에서 파일을 복사에서 옮기는 코드
root - 000 - file.file
위의 구조로 되어있는 파일들을 전부 하나의 디렉토리로 파일들을 옮기는 것임
아직 3중 4중이나 다른 다양한 형태에 대한 코드는 없음
"""


# # 이중으로 [폴더]-[폴더이름].jpg 이런식으로 있는 구조일 경우
# files_root = "J:/git/DeepGuider/bin/data/YorkUrbanDB"
# file_list = os.listdir(files_root)
# dst_root = 'J:/git/DeepGuider/bin/data/YUD'
# for f in file_list:
#     if '.' not in f:
#         filename = f"{f}.jpg"
#         from_filename = f"{files_root}/{f}/{filename}"
#         to_filename = f"{dst_root}/{filename}"
#         print(f"{from_filename}\t{to_filename}")
#         shutil.copy(from_filename, to_filename)
# #         pass

def copy_all_file(dir_root, dst_root, format='.jpg'):
    # for su3 case
    # dir_root = "C:/git/DeepGuider/bin/data/su3"
    # dst_root = 'C:/git/DeepGuider/bin/data/su3_images'

    dir_list = os.listdir(dir_root)
    
    for d in dir_list: # TODO : tqdm
        file_root = f"{dir_root}/{d}"
        file_list = os.listdir(file_root)
        for f in file_list:
            if format in f:
                filename = f"{f}{format}"
                
                from_filename = f"{file_root}/{f}"
                to_filename = f"{dst_root}/{d}_{f}"
    #             print(f"{from_filename}\n{to_filename}\n\n")
                shutil.copy(from_filename, to_filename)

# # validation dataset 만드는 코드
# # file list가 있는 txt 읽어서 파일들 옮겨주는 코드
# root_dir = "J:/git/DeepGuider/bin/data/tmm17"
# dst_dir = "J:/git/DeepGuider/bin/data/validation"
# txt_filename = f"{root_dir}/valid.txt"
# with open(txt_filename, 'r') as f:
#     lines = f.readlines()
# print(len(lines))
# for idx, filename in enumerate(lines):
#     # if idx<10:
#     filename = filename.strip()
#     from_filename = os.path.join(root_dir,filename)
#     to_filename = os.path.join(dst_dir,filename)
#     print(f"{idx}\t{from_filename}\t{to_filename}")
#     shutil.copy(from_filename, to_filename)

def file_copy_dir2dir(root_dir, su3_dirs, dst_dir):
    # su3 file 복사 => evaluation 하기 위해서
    print(f"{len(su3_dirs)}")
    for idx, su3_dir in enumerate(tqdm(su3_dirs)):
        # if idx<5:
        su3_files = os.listdir(os.path.join(root_dir,su3_dir))
        su3_files = [f for f in su3_files if ".npz" in f]
        # print(f"files : {len(su3_files)}")
        for su3_file in su3_files:
            from_filename = os.path.join(root_dir, su3_dir, su3_file)
            to_filename = os.path.join(dst_dir, f"{su3_dir}_{su3_file}")
            shutil.copy(from_filename, to_filename)

def file_copy_txt(txt_filename, root_dir="", dst_dir=""):
    """
    tmm17-valid.txt 를 dst_dir 에 옮기는 코드
    """
    with open(txt_filename, 'r') as f:
        filename_list = f.readlines()
        print(len(filename_list))
        for filename in filename_list:
            filename = filename.strip()
            from_filename = f"{root_dir}/{filename[:-4]}.txt"
            from_filename=from_filename.replace('ava', "AVA_landscape")
            from_filename=from_filename.replace('flickr', "Flickr")
            to_filename = f"{dst_dir}/{filename[:-4]}.txt"
            print(f"from {from_filename}\nto {to_filename}")
            shutil.copy(from_filename, to_filename)


def su3file_copy_sampling(root_path_img, root_path_label, dst_path_img, dst_path_label, sample_N=2000):
    """
    su3 데이터 샘플링해서 경로에 저장해줄 예정
    """
    file_img_list = os.listdir(root_path_img)
    sample_list = random.sample(file_img_list, sample_N)
    sample_list = [s.split('.')[0] for s in sample_list]
    print(sample_list[:5])
    for samplename in sample_list:
        from_filename1 = os.path.join(root_path_img, f"{samplename}.png")
        to_filename1 = os.path.join(dst_path_img, f"{samplename}.png")

        from_filename2 = os.path.join(root_path_label, f"{samplename}_label.npz")
        to_filename2 = os.path.join(dst_path_label, f"{samplename}_label.npz")
        
        shutil.copy(from_filename1, to_filename1)
        shutil.copy(from_filename2, to_filename2)



def main():
<<<<<<< Updated upstream
    # # valid.txt 안에 있는 파일들 옮겨주는 코드
    # root_dir ="D:/git/DeepGuider/bin/data/tmm17/vp-labels"
    # dst_dir = "D:/git/DeepGuider/bin/gt_valid"
    # txt_filename= "D:/git/DeepGuider/bin/data/tmm17/valid.txt"
    # file_copy_txt(txt_filename, root_dir, dst_dir)

    # # su3 file copy to dst_root
    # dir_root = "C:/git/DeepGuider/bin/data/su3"
    # dst_root = 'J:/git/DeepGuider/bin/data/su3_labels'
    # copy_all_file(dir_root, dst_root, format='.npz')

    # # su3 - sampling and copying img, label to each directory
    # root_path_img = "J:/git/DeepGuider/bin/data/su3_images"
    # root_path_label = "J:/git/DeepGuider/bin/data/su3_labels"
    # dst_path_img = "J:/git/DeepGuider/bin/data/gt_su3_sample"
    # dst_path_label = "J:/git/DeepGuider/bin/data/gt_su3_sample_labels"
    # su3file_copy_sampling(root_path_img, root_path_label, dst_path_img, dst_path_label, sample_N=2000)
=======
    # valid.txt 파일들 옮기기
    root_dir ="D:/git/DeepGuider/bin/data/tmm17/vp-labels"
    dst_dir = "D:/git/DeepGuider/bin/gt_valid"
    txt_filename= "D:/git/DeepGuider/bin/data/tmm17/valid.txt"
    file_copy_txt(txt_filename, root_dir, dst_dir)
>>>>>>> Stashed changes


    # su3 file copy
    root_dir = "/Volumes/새 볼륨/git/DeepGuider/bin/data/su3"
    dst_dir = "/Volumes/새 볼륨/git/DeepGuider/bin/data/gt_su3"

    su3_dirs = os.listdir(root_dir)
    
    file_copy_dir2dir(root_dir, su3_dirs, dst_dir)

if __name__=="__main__":
    main()