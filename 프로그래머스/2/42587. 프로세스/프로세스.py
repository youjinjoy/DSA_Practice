from collections import deque

def solution(priorities, location):
    h=[]
    q=deque()
    answer = 0

    for i in range(len(priorities)):
        q.append((priorities[i],i))
        
    priorities.sort()

    while len(priorities)!=0:
        answer+=1
        m=priorities.pop()
        while q[0][0]<m:
            q.append(q.popleft())
        if q.popleft()[1]==location:
            break

    return answer
