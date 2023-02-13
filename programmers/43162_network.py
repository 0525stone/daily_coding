"""
DFS로 문제 풀이
"""

# pass 한 솔루션
def solution_DFS(n, computers):
    print(f"{n}\t{computers}")
    answer = 0
    visited = [False for i in range(n)]
    print(visited)
    for com in range(n):
        
        if visited[com]==False:
            DFS(n, computers, com, visited)  # visited 가 계속 업데이트가 되는거야???
            answer+=1
        print(visited)
    return answer
    
def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)
                

def solution(n, computers):

    visited = [False for _ in range(n)]
    answer = 0
    for pos in range(n):
        if visited[pos]==False:
            BFS(n, computers, visited, pos)
            answer+=1
    return answer

def BFS(n, computers, visited, pos):
    visited[pos] = True
    q = []
    q.append(pos)
    while q:
        pos = q.pop(0)
        visited[pos] = True
        for connect in range(n):
            if connect != pos and computers[pos][connect] == 1:
                if visited[connect] == False:
                    q.append(connect)

if __name__=="__main__":
    
    # test case 추가해서 답 확인해주기
    n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    answer=solution(n, computers)
    assert answer==2, answer

    n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    answer=solution(n, computers)
    assert answer==1, answer

    print("all done")

