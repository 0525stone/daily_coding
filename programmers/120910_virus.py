"""
프로그래머스 세균증식 문제
"""

def solution(n, t):
    answer = n
    # answer = [n*2 for _ in range(t)][-1]
    for _ in range(t):
        answer *= 2
    
    return answer

# 정답
def solution(n, t):
    return n << t


if __name__=="__main__":
    n, t = [2, 10]
    answer = solution(n, t)
    assert answer==2048, answer
    
    n, t = [7, 15]
    answer = solution(n,t)
    assert answer==229376, answer

    print('all done')