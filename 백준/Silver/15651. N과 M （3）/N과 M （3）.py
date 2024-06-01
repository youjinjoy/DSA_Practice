import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split(' '))

def dfs(depth,current):
  if depth == M:
    print(' '.join(map(str,current)))
    return

  for i in range(1,N+1):
    dfs(depth+1,current+[i])

dfs(0,[])