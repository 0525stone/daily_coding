# 6090 ~ 6094

# 6089



# 6090
def sol_6090(c_):
    # c = input()
    # print(c_)
    c = c_.split(' ')
    a,m,d,n = int(c[0]), int(c[1]), int(c[2]), int(c[3])
    # print()
    result = a
    for i in range(n-1):
        result = result*m+d

    print(result)
# c = '1 -2 1 8'
# sol_6090(c)

# 6091
def sol_6091():
    c = input()
    c = '3 7 9'
    c_ = c.split(' ')
    a,b,c = int(c_[0]), int(c_[1]), int(c_[2])
    i = 1
    while True:

        if(i%a == 0 and i%b ==0 and i%c ==0):
            print(i)
            break

        i = i+1
# sol_6091()

# 6092
import numpy as np

def sol_6092():
    '''
    메모리 : 158264
    시간 : 148
    '''

    n = int(input())
    a = input().split()
    d = np.zeros(23)

    for i in range(n):
        a[i]= int(a[i])-1
        d[a[i]] = d[a[i]] + 1

    for i in range(len(d)):
        print(int(d[i]), end=' ')

def sol_6093():
    '''
    메모리 : 28156
    시간 : 25
    '''

    n =  int(input())
    a = list(map(int,input().split()))

    for i in range(len(a)):
        a[i] = int(a[i])

    for i in range (len(a)-1,-1,-1):
        print(int(a[i]),end = ' ')

def sol_6094():
    """
    메모리 : 27724
    시간 : 16
    """
    n =  int(input())
    a = list(map(int,input().split()))
    min = int(a[0])

    for i in range(len(a)):
        a[i] = int(a[i])
        if(min > a[i]):
            min = a[i]

    print(min)