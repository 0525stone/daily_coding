import os
import pandas as pd




def main():
    root_dir = "./data/jooui/adult"
    list_files = os.listdir(root_dir)

    print(f"files : {len(list_files)}")

    for idx, filename in enumerate(list_files):
        file_dir = os.path.join(root_dir, filename)
        if idx == 0:
            df = pd.read_csv(file_dir)
            print(f"column line : {len(df['ID'])}")
        else:
            new_df = pd.read_csv(file_dir)
            merged_df = df.merge(new_df, on='ID', how='outer')
    savename = os.path.join(root_dir, 'merged_file.csv')
    merged_df.to_csv(savename, index=False)
if __name__ == "__main__":
    main()