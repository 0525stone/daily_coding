"""
게임 맵 최단거리
- 
"""
import sys
from collections import deque


# Pass test
def solution(maps):
    """
    전체 게임맵에 장애물 0, 길 1을 채워놓고
      각 길에 대해서 몇번째에 도착하는지 숫자를 채워넣어줌 d + 1 이런식으로
      최종 목적지에 몇의 숫자가 들어있는지 확인하기
    """
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    map_x, map_y = (len(maps[0]), len(maps))

    answer = 0
    q = deque([(0,0,1)])

    # 일단 시작점을 q 에 넣어주고 while문 시작하면 됨

    while q:
        x, y, d = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx > -1 and ny > -1 and nx < map_x and ny < map_y:
                if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:
                    maps[ny][nx] = d + 1
                    if nx == map_x - 1 and ny == map_y - 1:
                        return d+1
                    q.append((nx, ny, d+1))




    
    return -1


if __name__=="__main__":

    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    answer = solution(maps)
    assert answer==11, answer

    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    answer = solution(maps)
    assert answer==-1, answer

    print("all done")
    # input1 = sys.stdin.readline()

    # print(input1)