
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



# trial 1 : 시간 초과
import itertools
def make_biggest_num1(numbers):
    """
    1. numbers의 원소 갯수를 갖고, index를 정렬하여, 컴프리헨션으로 순서 바꾼 list만들고, join으로 하나의 string으로 합쳐주고 int() 크기 비교로 하는건 어떨까?
    2. 각 원소의 첫번째 숫자만 갖고 tuple, dictionary를 만들고, 숫자 크기 순으로 합치게 하여 크기 비교를 하는건 어떨까? -> 안좋은 듯
    """
    answer = '0'
    # 1. permutation
    numbers = [str(num) for num in numbers]
    perm_list = list(itertools.permutations(numbers, len(numbers)))
    perm_list = sorted(perm_list, reverse=True)
    # print(perm_list)
    
    for p in perm_list:
        temp = ''.join(p)
        if perm_list[0][0]!=p[0][0]:
            break
        if int(temp)>int(answer):
            answer = temp
            # print(answer)
    return answer

    # # 2. 튜플 만들기. 첫글자, index
    # t_numbers = [(str(number)[0], idx) for idx, number in enumerate(numbers)]
    # print(t_numbers)

    # list_candidate = sorted(t_numbers, key=lambda x: x[0], reverse=True)
    # print(list_candidate)

    # for s in numbers:
    #     answer += s
    # return answer

# trail 2

def sort_num_cluster(cluster):
    print(f'sort num cluster\t{cluster}')
    answer = '0'
    numbers = [str(num) for num in cluster]
    perm_list = list(itertools.permutations(numbers, len(numbers)))
    # print(perm_list)
    for p in perm_list:
        temp = ''.join(p)
        # print(temp)
        # if perm_list[0][0]!=p[0][0]:
        #     break
        if int(temp)>int(answer):
            answer = temp
    print(answer)
    return answer


def make_biggest_num(numbers):
    """
    1부터 9까지 각각 군집을 만들어서 그 안에서 sort 해주고, 전체 다 합쳐주는 식으로 하면?
    
    각 군집에 대하여, 제일 큰 수를 뽑아주는 걸 확인하는 코드
    """
    # make number cluster   - make_num_cluster
    numbers = [str(number) for number in numbers]
    num_dict = {str(i):[] for i in range(9,0,-1)}

    # 이걸 comprehension 으로 할 수 있나??
    for number in numbers:
        num_dict[number[0]].append(number)
    # print(num_dict)

    temp = []
    for d in num_dict.keys():
        if num_dict[d]:
            num_dict[d] = sorted(num_dict[d], reverse=True)
            # temp.extend(num_dict[d])
            sorted_num_dict = sort_num_cluster(num_dict[d])
            temp.extend(sorted_num_dict)
    print(temp)


    answer = ''.join(temp)
    # print(answer)
    return answer


def main():

    # sort num cluster test
    assert (sort_num_cluster([60,6,6523,67,659]))=="676659652360"

    print('sort num cluster test done')



    assert make_biggest_num([60,6,5,67])=="676605"
    print('third done')

    print(make_biggest_num([6, 10, 2]))
    assert make_biggest_num([6, 10, 2])=="6210"
    print('first done')

    assert make_biggest_num([3, 30, 34, 5, 9])=="9534330"
    print('second done')

    



if __name__=='__main__':
    main()