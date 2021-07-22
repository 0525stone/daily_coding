"""
문제 설명
대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.

'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

제한사항
문자열 s의 길이 : 50 이하의 자연수
문자열 s는 알파벳으로만 이루어져 있습니다.

"""


def solution1(s):
    answer = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    p = 0
    y = 0
    s = s.lower()
    for i in s:
        if i=='p':
            p = p+1
        elif i=='y':
            y = y+1
    if p==y: return True
    else: return False

# string .count 로 문자열 확인 가능
def solution2(s):
    return s.lower().count('p') == s.lower().count('y')

s = "pPoooyY"	# true
s = "Pyy"	    # false

ans = solution1(s)
print(ans)