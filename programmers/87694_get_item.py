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
    answer = 0
    q = deque([characterX, characterY, 0])

    while 1:



        if cx==itemX and cy==itemY:
            return answer

    check_rec(rectangle, characterX, characterY)
        


    return answer

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

