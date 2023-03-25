"""
templete for programmers
"""
def make_map(V, bridge):
    m = [[0]*V for _ in range(V)]
    for b in bridge:
        m[b[0]-1][b[1]-1] = 1
        m[b[1]-1][b[0]-1] = 1
    return m

def DFS(iland, m, visited):
    visited[iland] = True
    for connect in range(len(visited)):
        if m[iland][connect]:
            if visited[connect]==False:
                DFS(connect, m, visited)
                


def solution(V, bridge):
    """
    연결된 섬의 군집을 구해야함
    DFS
    """
    answer = -1
    visited = [False for _ in range(V)]
    m = make_map(V, bridge)
    for iland in range(V):
        if visited[iland]==False:
            DFS(iland, m, visited)
            answer+=1

    return answer


if __name__=="__main__":
    
    V = 5
    bridge = [[1,2],[2,3],[4,5]]
    # test case 추가해서 답 확인해주기
    answer=solution(V, bridge)
    assert answer==1, answer
    print("done")

    V = 6
    bridge = [[1,2],[2,3],[4,5]]
    answer=solution(V, bridge)
    assert answer==2, answer

    
    print("all done")

