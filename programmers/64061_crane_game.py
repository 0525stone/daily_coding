


def move(i,board, baguni):
    for n in range(len(board[i])):
        if(board[i][n] != 0):
            baguni


def solution(board, moves):
    baguni = []
    answer = 0
    print(board)
    for i in range(len(board)):
        print(board[i])

    for i in range(len(moves)):
        move(i,board,baguni)

    # answer = 0

    print(answer)
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
ans=solution(board,moves)
# print(ans)