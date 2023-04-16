import os
import shutil

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

# for su3 case
dir_root = "C:/git/DeepGuider/bin/data/su3"
dir_list = os.listdir(dir_root)
dst_root = 'C:/git/DeepGuider/bin/data/su3_images'
for d in dir_list: # TODO : tqdm
    file_root = f"{dir_root}/{d}"
    file_list = os.listdir(file_root)
    for f in file_list:
        if '.png' in f:
            filename = f"{f}.jpg"
            
            from_filename = f"{file_root}/{f}"
            to_filename = f"{dst_root}/{d}_{f}"
#             print(f"{from_filename}\n{to_filename}\n\n")
            shutil.copy(from_filename, to_filename)
