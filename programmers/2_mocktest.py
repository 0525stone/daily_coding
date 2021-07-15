'''
문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.
'''

import numpy as np


def solution(answers):
    p_1 = [1, 2, 3, 4, 5]
    p_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    stu_1 = [p_1[i % 5] for i in range(len(answers))]
    stu_2 = [p_2[i % 8] for i in range(len(answers))]
    stu_3 = [p_3[i % 10] for i in range(len(answers))]

    sco_1 = 0
    sco_2 = 0
    sco_3 = 0
    for a, b, c, d in zip(answers, stu_1, stu_2, stu_3):

        if (a == b):
            sco_1 += 1
        if (a == c):
            sco_2 += 1
        if (a == d):
            sco_3 += 1
    score_list = [sco_1, sco_2, sco_3]

    max_ = np.max(score_list)
    max_in = np.where(score_list == max_)[0] + 1

    answer = max_in

    answer = np.ndarray.tolist(answer)  # 이게 제일 중요한 파트(json serialize 안된다는 에러 방지용)

    return answer


print('start')
answers = [1,2,3,4,5]
# answers = [1,3,2,4,2]

result = solution(answers)
print(result)