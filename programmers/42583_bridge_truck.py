"""
스택/큐

다리를 지나는 트럭 문제
"""
def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = [0]*bridge_length
    while truck_weights:
        bridge.pop(0)
        if (sum(bridge)+truck_weights[0])<=weight:
            bridge.append(truck_weights[0])
            truck_weights.pop(0)
            assert len(bridge)==bridge_length
        else:
            bridge.append(0)
        answer+=1
    if sum(bridge):
        answer+=bridge_length

    return answer



if __name__=="__main__":

    bridge_length, weight, truck_weights = 100, 100, [10]
    answer = solution(bridge_length, weight, truck_weights)
    assert answer==101, answer

    bridge_length, weight, truck_weights = 100, 100, [10,10,10,10,10,10,10,10,10,10]
    answer = solution(bridge_length, weight, truck_weights)
    assert answer==110, answer
    print("done")

    bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]
    answer = solution(bridge_length, weight, truck_weights)
    assert answer==8, answer

    print("all done")