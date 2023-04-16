import numpy as np


class su3_file():
    def __init__(self, filename):
        self.filename = filename
        self.contents = np.load(filename)
        print(self.contents['vpts'])
    



def main():
    npz_filename = "data/0000_0_label.npz"
    s = su3_file(npz_filename)


if __name__=="__main__":
    main()