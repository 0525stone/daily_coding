"""
문제 설명
String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

제한 사항
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
"Kim"은 반드시 seoul 안에 포함되어 있습니다.
"""

def solution(seoul):
    for i,kim in enumerate(seoul):
        if(kim == "Kim"):
            print('Kim is at ',i)

def others(seoul):
    """
    List명.index(값) -> Np.where 이랑 똑같은 동작하는애. 앞쪽에 있는 것 하나만 찾을 수 있음... 중복값 index는 못함
    """
    print(seoul.index('Kim'))
    return "김서방은 {}에 있다".format(seoul.index('Kim'))


seoul = ["Jane", "Kim","John","Kim"]
solution(seoul)
answer = others(seoul)
print(answer)