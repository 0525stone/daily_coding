"""
문제 설명
가로 길이가 Wcm, 세로 길이가 Hcm인 직사각형 종이가 있습니다.
종이에는 가로, 세로 방향과 평행하게 격자 형태로 선이 그어져 있으며, 모든 격자칸은 1cm x 1cm 크기입니다.
이 종이를 격자 선을 따라 1cm × 1cm의 정사각형으로 잘라 사용할 예정이었는데, 누군가가 이 종이를 대각선 꼭지점 2개를 잇는 방향으로 잘라 놓았습니다.
그러므로 현재 직사각형 종이는 크기가 같은 직각삼각형 2개로 나누어진 상태입니다.
새로운 종이를 구할 수 없는 상태이기 때문에,
    이 종이에서 원래 종이의 가로, 세로 방향과 평행하게 1cm × 1cm로 잘라 사용할 수 있는 만큼만 사용하기로 하였습니다.
가로의 길이 W와 세로의 길이 H가 주어질 때, 사용할 수 있는 정사각형의 개수를 구하는 solution 함수를 완성해 주세요.

제한사항
W, H : 1억 이하의 자연수


"""


# 웃기게도 x2를 return에 해주는 게 매번 2를 곱한걸 더해주는 것보다 더 빠(미세하지만 확실한 차이를 보)
def solution(w,h):
    answer = 0
    # gap = h//w패
    # for i in range(1,h):
    #     answer=answer+i*


    for idx, _w in enumerate(range(1,w),1):
        answer = answer+ idx*h//w
    return answer*2


# h//w를 gap으로 바꿔서 한거는 왜 아예 실패가떠?????
# gap 아닌 건 하나가 시간초과였고
# gap으로 한건 그냥 실
def solution(w, h):
    answer = 0

    for i in range(1,w):
        answer = answer + i*h//w
        print(answer)

    return answer * 2
import math

def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))


w, h = 8, 12 # 80
answer = solution(w,h)
print(answer)


