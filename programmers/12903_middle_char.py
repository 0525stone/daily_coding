"""
문제 설명
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
s는 길이가 1 이상, 100이하인 스트링입니다.


solution
    for 문에 인덱스랑 문자열 하나씩 읽어들여서 짝수면 두개, 홀수면 하나 return 시킴
"""


def solution(s):
    # print(s)
    # print(len(s))
    if(len(s)%2 == 0):
        print(s[len(s)//2-1:len(s)//2+1])
    else:
        print(s[len(s)//2])
    # # for i in enumerate(i,s)
    # for i in s:
    #     print(i)


def others(str):
    print(str[(len(str)-1)//2:len(str)//2+1])



s = "abcde"
# s = "qwer"
solution(s)
others(s)