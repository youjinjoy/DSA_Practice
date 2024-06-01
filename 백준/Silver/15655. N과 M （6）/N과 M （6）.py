import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))

def dfs(depth,start,current):
  if depth == M:
    print(' '.join(map(str,current)))
    return

  for i in range(start,N):
      dfs(depth+1,i+1,current+[arr[i]])

arr.sort()
dfs(0,0,[])