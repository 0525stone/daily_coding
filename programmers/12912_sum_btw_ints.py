"""
문제 설명
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

제한 조건
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.
"""

# 백준을 위한 입력 받는 방법
# 백준 : pypy3 가 python3 보다 더 빨리 동작
# 반복문으로 여러 입력을 받아야 할 때는 꼭 sys.stdin.readline 으로..
import sys
input = sys.stdin.readline

def solution(a,b):

    if a<b:
        answer = sum(range(a,b+1,1))
    else:
        answer = sum(range(b,a+1,1))
    print(answer)

def others(a, b):
    """
    확실히 내 코드보다 훨씬 간결하고 가독성이 좋음...
    """
    if a > b: a, b = b, a

    return sum(range(a,b+1))

# a, b = 3,5
a, b = 5,3
# a, b = 3,3

solution(a, b)
