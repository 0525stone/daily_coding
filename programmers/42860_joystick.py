"""



"""

def solution1(name):
    temp = 0
    for ch in name:
        print(f'{ch} : {ord(ch)}, {temp}')
        if(ord(ch)>78):
            temp = temp + 90-ord(ch)+1
        else:
            temp = temp + ord(ch)-65
        temp =temp+1
    print('check : ',name[-1])
    if len(name)==3 and name[1]=="A":
        temp = temp-1
    return temp-1


def solution(name):

    answer = 0
    temp = 0
    for ch in name:
        for i in range(65,91):

            if ch==chr(i):
                print(chr(i))
                break
            temp = temp + 1  # 다음 알파벳 확인
        print(ch,temp)
        temp = temp+1 # 다음 문자로 넘어가는 joystick




    return temp#answer


name = "JEROEN" # 56
name = "JAN"  # 23

answer = solution1(name)

print(answer)

print(ord("A"))
# print(chr(65))
# print(chr(66))
# print(chr(89))
# print(chr(90))

# for i in range(65,91):
#     print(i)