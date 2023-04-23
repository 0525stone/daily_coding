import numpy as np


class su3_file():
    def __init__(self, filename):
        self.filename = filename
        self.contents = np.load(filename)
        vpts = self.contents['vpts']
        print(vpts)
        y,x = self.to_pixel(vpts)
        print(f"vpts 결과 {x}, {y}")
    def to_pixel(self, vpts, focal_length=1.0, h=512, w=512): # 기존 h=480, w=640
        x = vpts[:,0] / vpts[:, 2] * focal_length * max(h, w)/2.0 + w//2
        y = -vpts[:,1] / vpts[:, 2] * focal_length * max(h, w)/2.0 + h//2
        return y, x
    

def main():
    npz_filename = "data/0000_0_label.npz"
    s = su3_file(npz_filename)


if __name__=="__main__":
    main()