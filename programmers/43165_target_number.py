"""
문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.

"""

def target_number(numbers, target):
    """
    queue 필요
    - +먼저하고 -한 뒤에는 queue에서 빼냄 
    
    포인터 위치도 필요한가..?

    끝까지 온 경우, target과 비교후 answer 더해줄지 말지 결정
    

    """
    answer = 0
    targets = [0]
    for num in numbers:
        temp = []
        for tgt in targets:
            temp.append(tgt+num)
            temp.append(tgt-num)
        targets = temp
        # print(targets)
    answer = targets.count(target)
    # print(answer)
    return answer

import random

from numpy import number

def generate_test_case():
    """
    제한사항

    주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
    각 숫자는 1 이상 50 이하인 자연수입니다.
    타겟 넘버는 1 이상 1000 이하인 자연수입니다.
    """
    num = random.randrange(2,21)
    
    numbers = [random.randrange(1,51) for _ in range(num)]
    target = random.randrange(1,1001)
    return numbers, target


def main():
    assert target_number([1, 1, 1, 1, 1], 3)==5
    print('first done')
    assert target_number([4, 1, 2, 1], 4)==2
    print('second done')

    for _ in range(20):
        n1, t1 = generate_test_case()
        print(f'random test case\nnumbers\t{n1}\ntarget\t{t1}')
    
    print('example test answer : ',target_number([9, 36, 15, 36, 8, 47, 19, 40, 14, 1, 46, 34, 34, 2, 34, 36, 18, 26, 29, 49], 159))
    print('example test answer : ',target_number([11, 47, 38, 29, 23, 10, 36, 1, 29, 49],14))
    

if __name__=='__main__':
    main()