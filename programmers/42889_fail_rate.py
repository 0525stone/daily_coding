"""
실패율
failture_rate1.png

슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다. 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다. 역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오렐리를 위해 실패율을 구하는 코드를 완성하라.

실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

제한사항
스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
stages의 길이는 1 이상 200,000 이하이다.
stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

"""

# trial 1
def update_stages(stages_dict, stage):
    for n in range(1,stage+1):
        stages_dict[n] += 1

    return stages_dict

import numpy as np

def failure_rate1(N, stages):
    answer = []


    stages_arrived = {n : 0 for n in range(1,N+2)}
    stages_stay = {n : 0 for n in range(1,N+2)}
    print(stages_arrived)

    # stage 별 도착, stay에 대한 dictionary
    for stage in stages:
        stages_arrived = update_stages(stages_arrived, stage)
        stages_stay[stage] += 1
    
    print(f'stay\t{stages_stay}')   
    print(f'arrived\t{stages_arrived}')

    # list 각 스테이지별 실패율
    failure_list = [1 if stages_arrived[n]==0 else float(1-stages_stay[n]/stages_arrived[n]) for n in range(1,N+1)]  
    # failure_list = [float(1-stages_stay[n]/stages_arrived[n]) for n in range(1,N+1)]  

    answer = np.argsort(failure_list)
    answer = [int(ans+1) for ans in answer]
    print(f'answer\t{answer}')
    return answer


# trial 2 이자 final 
def failure_rate(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)

        if length ==0:
            fail = 0
        else:
            fail = count/length
        length -= count

        answer.append((i,fail))

    answer = sorted(answer, key=lambda x: x[1], reverse = True)
    answer = [i[0] for i in answer]

    return answer



# trial 3 실패(trial 2만 성공) -> 왜 failure을 1-fail로 하면 안될까??
def failure_rate2(N, stages):
    answer = []
    length = len(stages)

    for i in range(1, N+1):
        count = stages.count(i)

        if length ==0:
            fail = 0
        else:
            fail = count/length
        length -= count

        answer.append(1-fail)
        # answer.append(fail)

    answer = np.argsort(answer)
    # answer = sorted(answer, key=lambda x: x[1], reverse = True)
    # answer = [i[0] for i in answer]
    answer = [ans+1 for ans in answer]
    

    return answer

def main():
    assert failure_rate(5,[2, 1, 2, 6, 2, 4, 3, 3])==[3,4,2,1,5]
    print('first done\n')
    assert failure_rate(4,[4,4,4,4,4])==[4,1,2,3]
    print('second done\n')
    # print(failure_rate(5,[4,4,2,2,5,3,6,3,2,1]))
    assert failure_rate(5,[4,4,2,2,5,3,6,3,2,1])==[4, 5, 2, 3, 1]
    print('third done\n')
    # print(failure_rate(8,[1,1,1,1,1,1,1,1,1,1]))
    assert failure_rate(8,[1,1,1,1,1,1,1,1,1,1])==[1, 2, 3, 4, 5, 6, 7, 8]
    print('fourth done\n')
    print(failure_rate(8,[9,9,9,9,9,9,9,9,9,9]))
    print(failure_rate2(8,[9,9,9,9,9,9,9,9,9,9]))
    print('fifth done\n')
    print(failure_rate(10,[9,9,9,9,9,9,9,9,9,9]))
    print(failure_rate2(10,[9,9,9,9,9,9,9,9,9,9]))
    print('sixth done')
    print(failure_rate(8,[1,2,4,5,6,8]))
    print(failure_rate2(8,[1,2,4,5,6,8]))

if __name__=="__main__":
    main()