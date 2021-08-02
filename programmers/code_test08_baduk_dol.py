"""
바둑돌 놓기


"""




# num_p = 5
# points = [(1,1),(2,2),(3,3),(4,4),(5,5),]
#
import numpy as np

def baduk_dol(num_p, points):

    board = np.zeros((19,19))
    for _, point in enumerate(points):
        board[point[1]-1][point[0]-1] = 1

    print(board)

points = []

n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    points.append((a,b))


print('read done')
print(points)


baduk_dol(n, points)


"""
input
5 
1 1 
2 2 
3 3 
4 4 
5 5
"""