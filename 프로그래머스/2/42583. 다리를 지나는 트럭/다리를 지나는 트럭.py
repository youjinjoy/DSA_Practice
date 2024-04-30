from collections import deque

def solution(bridge_length, weight, truck_weights):
    w = 0
    time = 0
    q = deque([0 for _ in range(bridge_length)])
    for truck in truck_weights:
        if w+truck > weight:
            while True:
                w -= q.popleft()
                time+=1
                if w+truck > weight:
                    q.append(0)
                else:
                    q.append(truck)
                    w += truck
                    break
        else:
            w -= q.popleft()
            q.append(truck)
            w += truck
            time += 1

    time += bridge_length
    
    return time