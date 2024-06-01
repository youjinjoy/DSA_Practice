import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split(' '))

used = [False] * (N+1)
current = []

def dfs(depth,start):
  if depth == M:
    print(' '.join(map(str,current)))
    return

  for i in range(start,N+1):
    if not used[i]:
      current.append(i)
      used[i]=True
      dfs(depth+1,i+1)
      current.pop()
      used[i]=False

dfs(0,1)