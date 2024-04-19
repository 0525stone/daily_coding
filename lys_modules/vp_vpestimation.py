import os
import json

def main():
    root_dir = "../data/VP_output"
    list_file = os.listdir(root_dir)
    vp_check(list_file, root_dir)

def vp_check(list_file, root_dir):
    print(len(list_file))
    for idx, file in enumerate(list_file):
        if idx < 10:
            file_dir = os.path.join(root_dir, file)
            print(file_dir)
            with open(file_dir, 'r') as f:
                json_data = json.load(f)
                # print(json.dumps(json_data) )
                print(json_data['vanishing_points'])



if __name__ == "__main__":
    
    file_dir = "C:/git/data/VP_output"
    file_dir = "../data/VP_output"
    list_file = os.listdir(file_dir)

    main()
    
    
    
    