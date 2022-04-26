"""
link : https://programmers.co.kr/learn/courses/30/lessons/42626

문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.


"""

# trial1
def make_scoville1(scoville, K):
    answer = 0
    scoville = sorted(scoville)
    num_scoville = len(scoville)
    # 모든 음식 스코빌 지수 K 이상 만들 수 없는 경우 -1 return 
    while 1:

        # 이미 전부 만족하는 경우에는 return 0
        if scoville[0]>=K:
            return num_scoville - len(scoville)
        if not scoville:
            return -1

        temp1 = scoville[0]
        temp2 = scoville[1]


        scoville[0] = temp1 + (2*temp2)
        scoville = sorted(scoville)    # 시간 초과가 나는 이유인 듯... -> np.min을 사용하면 될까?

        scoville.pop(0)

    return answer


import numpy as np

# make all food over scoville threshold(K) -> 효율성 테스트에서 시간 초과로 탈락(정확도는 100%)
def make_scoville2(scoville, K):

    answer = 0
    num_scoville = len(scoville)

    while 1:
        min1 = np.min(scoville)
        if min1>=K:
            return num_scoville - len(scoville)
        scoville.remove(min1)
        if not scoville:
            return -1
        min2 = np.min(scoville)
        scoville.remove(min2)

        # new_k = min1 + 2*min2

        scoville.append(min1 + 2*min2)
    return answer


# make all food over scoville threshold(K) -> 효율성 테스트에서 시간 초과로 탈락(정확도는 100%)
# np.min 보다는 일단 min이 훨씬 더 빠르게 하는 것 확인(30ms -> 6ms)
def make_scoville3(scoville, K):

    answer = 0
    num_scoville = len(scoville)

    # while 1:
    for _ in range(num_scoville):
        min1 = min(scoville)

        if min1>=K:
            return num_scoville - len(scoville)
        scoville.remove(min1)

        # if min1>=K:
        #     return num_scoville - len(scoville) + 1
        if not scoville:
            return -1
        
        min2 = min(scoville)
        scoville.remove(min2)

        # new_k = min1 + 2*min2

        scoville.append(min1 + 2*min2)
    return answer


# trial4
def make_scoville4(scoville, K):

    answer = 0
    num_scoville = len(scoville)

    # 모든 음식 스코빌 지수 K 이상 만들 수 없는 경우 -1 return 
    for _ in range(num_scoville):

        scoville = sorted(scoville)
        # 이미 전부 만족하는 경우에는 return 0
        if scoville[0]>=K:
            return num_scoville - len(scoville)


        temp1 = scoville[0]
        scoville = scoville[1:]
        if not scoville:
            return -1
        temp2 = scoville[0]
        scoville = scoville[1:]
        scoville.append(temp1 + (2*temp2))


    return answer


# trial4
def make_scoville(scoville, K):

    answer = 0
    num_scoville = len(scoville)

    # 모든 음식 스코빌 지수 K 이상 만들 수 없는 경우 -1 return 
    for _ in range(num_scoville):

        scoville = sorted(scoville)
        # 이미 전부 만족하는 경우에는 return 0
        if scoville[0]>=K:
            return num_scoville - len(scoville)


        temp1 = scoville[0]
        scoville = scoville[1:]
        if not scoville:
            return -1
        temp2 = scoville[0]
        scoville = scoville[1:]
        scoville.append(temp1 + (2*temp2))


    return answer


def main():
    a = [5,1,3,27,2,4]
    a = sorted(a)
    print(a)

    assert make_scoville([1, 2, 3, 9, 10, 12],7)==2
    print('test done')


if __name__=="__main__":
    main()