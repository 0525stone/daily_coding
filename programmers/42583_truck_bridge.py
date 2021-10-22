
"""
deque : https://chaewonkong.github.io/posts/python-deque.html

"""






from collections import deque


bridge_length = 2
weight = 10
truck_weight = [6,5,4,7]


cur = 0
bridge = deque()
truck = deque(truck_weight)
for i in range(bridge_length):
    bridge.append(0)

print(bridge)
time = 0
while True:

    cur = truck.pop()+cur

    if cur < weight:
        try:
            t_temp = truck.pop()
        except:
            t_temp = 0
        b_temp = bridge.pop()
        bridge.append(t_temp)
        cur = cur + t_temp - b_temp

    else:
        bridge.pop()
        bridge.append(0)
    print('bridge : ',bridge)
    print('truck : ',truck)
    time = time + 1
    if not (truck or cur):
        print('break1')
        break



print(time)