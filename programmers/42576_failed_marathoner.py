"""
완주하지 못한 마라톤 선수를 찾는 프로그램

문제 설명
- 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
- 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.




"""


def solution(participant, completion):
    answer = ''

    # # set으로 문제를 풀어보기 -> 안되네?????
    # print(f'participant : {participant}\ncompletion : {completion}')
    # answer = set(participant)- set(completion)
    # print(answer)

    # list로 문제 풀어보기 -> 답은 맞는데 효율성에서 통과 불가
    # answer = [ for name in participant if name in completion]
    # participant.sort()
    # completion.sort()
    # for name in completion:
    #     participant.remove(name)
    # answer = participant

    # zip으로 풀어보기 -> done
    participant.sort()
    completion.sort()

    for p,c in zip(participant,completion):
        if p!=c:
            return p

    return participant[-1]


def main():
    
    assert solution(["leo", "kiki", "eden"],["kiki", "eden"])=='leo'
    assert solution(["marina", "josipa", "nikola", "vinko", "filipa"],["marina", "josipa", "nikola", "filipa"])=='vinko'
    assert solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "mislav", "ana"])=='mislav'
    print('done testing')


if __name__=="__main__":
    main()