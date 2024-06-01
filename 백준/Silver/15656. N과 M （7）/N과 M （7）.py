import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))

def dfs(depth,current):
  if depth == M:
    print(' '.join(map(str,current)))
    return

  for i in range(0,N):
      dfs(depth+1,current+[arr[i]])

arr.sort()
dfs(0,[])