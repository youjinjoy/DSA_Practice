from collections import deque
import heapq

def solution(priorities, location):
    h=[]
    q=deque()
    for i in range(len(priorities)):
        q.append((priorities[i],i))
        heapq.heappush(h,-priorities[i])
    answer = 0

    while len(h)!=0:
        answer+=1
        m=-heapq.heappop(h)
        while q[0][0]<m:
            q.append(q.popleft())
        if q.popleft()[1]==location:
            break

    return answer