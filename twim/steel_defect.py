from twim import steel_img

class defect_steel(steel_img):
    def __init__(self, steel_img, blob_size, ):
        self.steel_img = steel_img
        self.blob_size = blob_size