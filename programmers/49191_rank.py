"""
순위 - 그래프

win_graph 와 lose_graph 를 각각 그리고 각 노드에 대해서 이기고 진 것을 카운트함
그 둘의 합이 n-1 이면 순위가 확정된 것임

"""

from collections import defaultdict


def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)

    for winner, loser in results:
        print(f"{winner} {loser}")
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)
    
    for i in range(1,n+1):
        for winner in win_graph[i]:
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:
            win_graph[loser].update(win_graph[i])
    
    for i in range(1,n+1):
        if len(win_graph[i])+len(lose_graph[i]) == n-1:
            answer+=1


    return answer


if __name__=="__main__":
    
    n, results = 5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    answer=solution(n, results)
    assert answer==2, answer

    print("all done")

