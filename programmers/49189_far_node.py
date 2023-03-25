"""
가장 먼 노드
"""
from collections import deque

def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])

def solution(n, edge):
    answer = 0
    visited = [-1]*(n+1)
    print(visited)
    adj = [[] for _ in range(n+1)]
    print(adj)
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    bfs(1, visited, adj)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer



if __name__=="__main__":
    

    for i in range(4):
        re = i+1
        for _ in range(3):
            re = re*(i+_)
            print(re)


    # test case 추가해서 답 확인해주기
    n, edge = 6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    answer=solution(n, edge)
    assert answer==3, answer
    print("done")


    print("all done")

