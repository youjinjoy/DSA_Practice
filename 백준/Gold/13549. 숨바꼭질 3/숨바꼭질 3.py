import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int,input().split(' '))
q = deque()

q.append(N)
cost = [-1]*100001
cost[N] = 0

while q:
  x = q.popleft()

  if x == K:
    print(cost[x])
    break

  if x*2<=100000 and (cost[x*2] == -1 or cost[x*2]>cost[x]):
    q.append(x*2)
    cost[x*2] = cost[x]

  if x+1<=100000 and (cost[x+1] == -1 or cost[x+1]>cost[x]) :
    q.append(x+1)
    cost[x+1] = cost[x]+1
    
  if x-1>=0 and (cost[x-1] == -1 or cost[x-1]>cost[x]):
    q.append(x-1)
    cost[x-1] = cost[x]+1

