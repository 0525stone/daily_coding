"""
완전탐색 밖에 답이 없는 듯
result는 n * (n+1) 보다 작은 수임
1부터 시작하여 연속되는 수(n)까지를 곱할 때, n*(n+1) 보다 작은 경우의 N을 구함
구한 N으로 모든 연속하는 수를 곱해서 Array 만들어주고 set, sorted 하여 결과 출력해주기
"""

def find_N(n):

    max_N = n*(n+1)
    result = 1
    N = 1
    while result*(result+1)<max_N:
        result*=N
        N+=1
    return N 

def fill_array(arr, N, n):
    new_arr = []
    for i in range(n):
        re = i + 1
        for _ in range(N-1):
            re = re*(i+_+1)
        new_arr.append(re)
        print(re, N)
    return arr.extend(new_arr)

# 문제마다 주어지는 형태 복사 붙여넣기하기
def solution(n):
    answer = 0
    N = find_N(n)

    arr = []
    if N==1:
        return 2
    for i in range(2,N+1):
        arr = fill_array(arr, i, n)

    arr = set(arr)
    arr = sorted(arr)
    return arr[n]


if __name__=="__main__":
    
    # test case 추가해서 답 확인해주기
    n = 1
    answer=solution(n)
    assert answer==2, answer
    print("done")

    n = 2
    answer=solution(n)
    assert answer==6, answer
    print("done")

    n = 4
    answer=solution(n)
    assert answer==20, answer
    print("done")

    n = 9
    answer=solution(n)
    assert answer==60, answer
    print("done")

    print("all done")

