"""
230603 parameter 관리


"""


dataset_parameters = {
    "su3" : {},
    "etri" : {},
    "flickr" : {},
    "ava" : {}
}

def dataset_reading_gt(dataset_name):
    """
    gt 를 읽는 방법이 다름.. => 그래픽 모델을 비전 모델로 바꾸기 위해서 su3의 경우 y 좌표에 대해서 -를 붙임
    나머지는 gt에 - 붙이는 것 없이 그대로 읽으면 됨
    """
    if dataset_name=="su3":
        pass

