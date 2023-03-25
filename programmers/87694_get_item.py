"""
templete for programmers
"""
from collections import deque

# 문제마다 주어지는 형태 복사 붙여넣기하기
def solution(rectangle, characterX, characterY, itemX, itemY):
    """
    어떤 사각형 테두리에 있는 것인지 확인하는 함수 필요
    바깥 테두리이어야함.. => 
    종료 조건 itemX, itemY 위치로 오게 되면 종료

    method
    1. map을 만들어서 위로 아래로 가는 것을 각각 구해보기?
    2. dfs로 구해보기

    
    """
    MAX = 50
    answer = 0
    maps = make_map(rectangle, characterX,characterY)
    q = deque([(characterX, characterY, 0)])
    visited = [[0 for _ in range(MAX)] for _ in range(MAX)]
    visited[characterX][characterY] = 1
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        x, y, d = q.popleft()
        if x==itemX and y==itemY:
            answer = d
            break
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if visited[nx][ny]==0 and maps[nx][ny]==1:
                q.append([nx,ny,d+1])
                visited[nx][ny] = visited[x][y]+1
    return answer



    # while 1:
    #     # 종료 조건
    #     if cx==itemX and cy==itemY:
    #         return answer
    return answer

def make_map(rectangle, characterX,characterY, MAX = 50):
    
    maps = [[9 for _ in range(MAX)] for __ in range(MAX)]
    for rec in rectangle:
        x1, y1, x2, y2 = rec
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    maps[i][j] = 0
                elif maps[i][j] != 0:
                    maps[i][j] = 1

    print(maps)

    return maps


def check_rec(rectangle, characterX, characterY):
    pass


if __name__=="__main__":
    
    # test case 추가해서 답 확인해주기
    rectangle, characterX, characterY, itemX, itemY = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8
    answer=solution(rectangle, characterX, characterY, itemX, itemY)
    assert answer==17, answer
    print('done')

    rectangle, characterX, characterY, itemX, itemY = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1
    answer=solution(rectangle, characterX, characterY, itemX, itemY)
    assert answer==11, answer
    print('done')

    rectangle, characterX, characterY, itemX, itemY = [[1,1,5,7]], 1, 1, 4, 7
    answer=solution(rectangle, characterX, characterY, itemX, itemY)
    assert answer==9, answer
    print('done')

    rectangle, characterX, characterY, itemX, itemY = [[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10
    answer=solution(rectangle, characterX, characterY, itemX, itemY)
    assert answer==15, answer
    print('done')

    rectangle, characterX, characterY, itemX, itemY = [[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3
    answer=solution(rectangle, characterX, characterY, itemX, itemY)
    assert answer==10, answer


    print("all done")

