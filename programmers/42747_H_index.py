
"""
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.



"""


"""
RuntimeError
https://www.secmem.org/blog/2020/09/19/rte/
1. 배열에 할당된 크기를 넘어서 접근했을 때
2. 전역 배열의 크기가 메모리 제한을 초과할 때
3. 지역 배열의 크기가 스택 크기 제한을 넘어갈 때
4. 0으로 나눌 떄
5. 라이브러리에서 예외를 발생시켰을 때
6. 재귀 호출이 너무 깊어질 때
7. 이미 해제된 메모리를 또 참조할 때
8. 프로그램(main 함수)이 0이 아닌 수를 반환했을 때
"""

# programmers
def solution_p(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# 런타임 에러
def solution(citations):

    citations = sorted(citations, reverse=True)
    answer = 1

    while True:
        try:
            if citations[answer-1]<answer:
                break
            answer = answer+1
        except:
            break
    return answer-1


citations = [3, 0, 6, 1, 5]	 #3
citations = [8, 6, 6, 5, 5]	 #
answer = solution(citations)
print(answer)
