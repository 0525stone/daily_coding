"""
link : https://programmers.co.kr/learn/courses/30/lessons/42586

문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

제한 사항
작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
작업 진도는 100 미만의 자연수입니다.
작업 속도는 100 이하의 자연수입니다.
배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

"""
def solution(progresses, speeds):
    """
    1. 제일 처음에 있는 것을 완료하는 시점에서,
        (100-progress)/speed
    2. 바로 뒤에 있는 것들이 100을 넘으면 pop 하고,
    3. 아닌 것들을 갖고 1 시작
    
    """
    answer = []
    
    while 1:
        temp = 0
        progress = progresses[0]
        speed = speeds[0]

        # progress day   
        # day = math.ceil((100-progress)/speed)     # ceil()로 하는게 더 나은 건가???? -> 바꿔서 제출해봤는데, 기존엔 되었던 것들에서도 런타임에러 뜸
        if (100-progress)%speed:
            day = (100-progress)//speed+1
        else: day = (100-progress)//speed

        # progress update
        progresses = [p+s*day for p, s in zip(progresses, speeds)]
        temp_progresses = progresses.copy()

        for p in temp_progresses:
            if p>=100:
                progresses.pop(0)
                speeds.pop(0)
                temp+=1
            else:
                break
        answer.append(temp)
        
        # 배포할 progress가 없으면 종료
        if not progresses:
            break

    return answer


def main():
    assert solution([93, 30, 55],[1, 30, 5])==[2,1]
    print('first done')
    assert solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])==[1,3,2]
    print('second done')


if __name__=="__main__":
    main()