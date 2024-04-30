from collections import deque

def solution(bridge_length, weight, truck_weights):
    w = 0
    time = 0
    q = deque([0 for _ in range(bridge_length)])
    for truck in truck_weights:
        while True:
            w -= q.popleft()
            time+=1
            if w+truck > weight:
                q.append(0)
            else:
                q.append(truck)
                w += truck
                break

    time += bridge_length
    
    return time