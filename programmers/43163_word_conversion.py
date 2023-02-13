"""
templete for programmers
"""
from collections import deque

# 문제마다 주어지는 형태 복사 붙여넣기하기
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [False for i in range(len(words))]
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt ==1 :
                    q.append([words[i], cnt+1])
                    V[i] = 1



    return answer



if __name__=="__main__":
    
    # test case 추가해서 답 확인해주기
    begin, target, words = ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    answer=solution(begin, target, words)
    assert answer==4, answer
    print('done')

    begin, target, words = ("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    answer=solution(begin, target, words)
    assert answer==0, answer

    print("all done")

