"""
문제 설명
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

제한 조건
n은 길이 10,000이하인 자연수입니다.

"""
import itertools

def solution_km(n):
    # 이터툴스로 이렇게 해서 마지막에 join으로 잘라서 출력
    itertools.cycle(['수','박'])

def solution(n):
    sb = '수박'
    return ''.join([sb[i%2] for i in range(n)])

def solution2(n):
    return ''.join(['수' if i%2==0 else '박' for i in range(n)])

def solution3(n):
    s = "수박"*n
    print(s[:n])
    return s[:n]

n=3
n=4
result = solution2(n)
print(result)