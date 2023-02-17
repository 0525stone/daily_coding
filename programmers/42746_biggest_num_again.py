"""
templete for programmers
"""
# numbers_str = [str(number) for number in numbers]
# numbers_str.sort(key=lambda num: num*3, reverse=True)
# return str(int(''.join(numbers_str)))


from itertools import permutations

def solution(numbers):
    # per_N = len(numbers)
    # numbers = [str(n) for n in numbers]
    # permut_list = list(permutations(numbers, per_N))
    
    # permut_list = sorted(permut_list)
    # print(permut_list)    
    # return str(max(permut_list))
    numbers = list(map(str, numbers))
    print(f"list {numbers}")
    numbers.sort(key=lambda x:x*3, reverse=True)
    print(f"list {numbers}")
    return str(int(''.join(numbers)))
    


if __name__=="__main__":
    
    # test case 추가해서 답 확인해주기
    numbers = [6, 10, 2]
    answer=solution(numbers)
    assert answer=="6210", answer
    print("done")

    numbers = [3, 30, 34, 5, 9]
    answer=solution(numbers)
    assert answer=="9534330", answer

    print("all done")

