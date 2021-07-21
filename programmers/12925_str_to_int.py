"""
문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

제한 조건
s의 길이는 1 이상 5이하입니다.
s의 맨앞에는 부호(+, -)가 올 수 있습니다.
s는 부호와 숫자로만 이루어져있습니다.
s는 "0"으로 시작하지 않습니다.

입출력 예
예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

"""



def solution1(s):

    if s[0] == '-':

        answer = -int(s[1:])

    answer = int(s)

    return answer



def solution2(s):

    return int(s)

# 프로그래머스
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        print(number)
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx) # 뒤에서부터 읽어와서 자릿수를 곱해주네..

    return result


# s = '1234'
s = '-1234'
ans2 = strToInt(s)
print(ans2)

# ans = solution2(s)
# print(s)