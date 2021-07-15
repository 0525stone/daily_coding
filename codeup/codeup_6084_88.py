# 6085 ~ 6089
def sol_6084():
    """
    메모리 : 27724
    시간 : 18
    """
    nums = input()
    num = nums.split(" ")
    h, b, c, s = int(num[0]), int(num[1]), int(num[2]), int(num[3])
    print('{:.1f} MB'.format(h*b*c*s/8/1024/1024))

def sol_6085():
    # Input
    # ? map으로 입력을 받으면 더 깔끔할 텐데...
    nums = input()
    num = nums.split(" ")

    n1 = int(num[0])
    n2 = int(num[1])
    n3 = int(num[2])

    # print('n1 : ',n1,' n2 : ',n2,' n3 : ',n3)

    # Process
    # input = [1024, 768, 24]
    #
    # n1 = 1024
    # n2 = 768
    # n3 = 24

    total = n1*n2*n3/8/1024/1024

    print('{:.2f}MB'.format(total))

def sol_6086():
    """
    메모리 : 27724
    시간 : 20
    """
    try:
        c = int(input())
    except ValueError as e:
        print("wrong data type")

    sum = 0
    i = 0
    while True:


        sum = sum+i
        if(sum>=c):
            break
        print(sum)
        i = i + 1
    print(sum)

def sol_6087():
    """
    메모리 : 27724
    시간 : 17

    시간복잡도 : O(n)?
    """

    try:
        c = int(input())
    except ValueError as e:
        print("wrong data type")

    for i in range(1,c+1):
        if(i%3 == 0):
            continue
        else:
            print(i, end=" ")

def sol_6088():
    """
    메모리 : 27724
    시간 : 17
    """
    nums = input()
    try:
        num = nums.split(" ")
        a = int(num[0])
        d = int(num[1])
        n = int(num[2])
    except:
        print("something is wrong")
    print(a+d*(n-1))


sol_6084()