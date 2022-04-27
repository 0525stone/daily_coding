"""
문제 설명
정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.


조합으로 경우의 수를 만들어서 하게 끔?


"""




def sum_two_num(numbers):
    
    answer = []
    idx_num = len(numbers)
    idxs = [(i,j) for i in range(idx_num) for j in range(i+1,idx_num)]
    # print(idxs)
    
    answer = [numbers[i[0]]+numbers[i[1]] for i in idxs]
    answer = list(set(answer))
    
    return answer



def main():

    for i in range(5,-1,-1):
        print(i)

    assert sum_two_num([2,1,3,4,1])==[2,3,4,5,6,7]
    print('first done')

    assert sum_two_num([5,0,2,7])==[2,5,7,9,12]
    print('second done')

    assert sum_two_num([])==[2,5,7,9,12]
    print('third done')


if __name__=='__main__':
    main()