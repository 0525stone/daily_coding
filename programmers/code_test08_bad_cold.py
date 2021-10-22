"""
독감예방 파티션 문제

입력
[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

"""
import numpy as np

SIZE = 5

def find_men(board):
    men = []
    table = []
    for i in range(SIZE):
        for j in range(SIZE):
            if (board[i][j]=='P'):
                men.append(i,j)
        table.append(list)
    return board, men

def check_distances(man):


def solution(boards):
    answer = []

    for board in boards:
        table, men = find_men(board)

        for man in men:
            check_distances(man)






# for _ in range(5):
#     a,b = map(int, input().split())
#     points.append((a,b))

# board = list(map(str,input()))
# print(board)
# # board = list(board)
# for i in range(5):
#     print(board[i])

boards = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

solution(boards)



