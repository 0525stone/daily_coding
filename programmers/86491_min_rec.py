"""
프로그래머스 최소직사각형
"""

# 문제마다 주어지는 형태 복사 붙여넣기하기
def solution(sizes):
    answer = 0
    long_ = [s[0]if s[0]>s[1] else s[1] for s in sizes]
    short_ = [s[0]if s[0]<s[1] else s[1] for s in sizes]
    print(f"long\t{long_}\nshort\t{short_}")
    answer = max(short_)*max(long_)
    return answer



if __name__=="__main__":

    sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    # test case 추가해서 답 확인해주기
    answer=solution(sizes)
    assert answer==4000, answer
    print("done")
    
    sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
    answer=solution(sizes)
    assert answer==120, answer
    print("done")

    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    answer=solution(sizes)
    assert answer==133, answer
    print("done")


    print("all done")

