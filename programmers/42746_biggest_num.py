
"""
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

solution:

1.입력 numbers를 decimal, 10이하의 number 유효숫자를 찾아서 분해해줌
2.유효숫자를 sorted(reversed=True)
3.string으로 붙여줌
4.실패

"""

# TODO:functools cmp_to_key 를 하면 뒤에 오는 것들 2개씩 인자로 받아서 연산해줌 -> 이거로 해봐야함





def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


def solution11(numbers):
    print(numbers)
    decimal = [-1 for _ in range(len(numbers))]
    print(decimal)
    num = {}

    a = [3,6,1,3,6]

    print(a)
    a.pop(3)
    print(a)


    data =[]
    # for i in range(5,-1,-1):
    for i in range(6):


        for idx,number in enumerate(numbers):

            if(number/(10**i))>0 and (number/(10**i))<10 and decimal[idx]==-1:
                numbers[idx] = number/(10**i)
                decimal[idx] = i
                data.append((numbers[idx],decimal[idx]))
                # num[str()]

    print(numbers)
    print(decimal)
    print(data)

    number_sorted = sorted(numbers,reverse=True)
    print(number_sorted)

    data_sorted = sorted(data,reverse=True)
    print(data_sorted)

    print(data_sorted[0][0]*(10**data_sorted[0][1]))
    # print(10**0)
    answer = ""
    for idx, data_ in enumerate(data_sorted):

        print(idx, data_)
        chk = int(data_[0]*(10**data_[1]))
        print(chk)
        answer = answer + str(chk)

    print(answer)
    return answer


number = [6, 10, 2]	        # "6210"
number = [3, 30, 34, 5, 9]	# "9534330"

ans = solution(number)
print(ans)
