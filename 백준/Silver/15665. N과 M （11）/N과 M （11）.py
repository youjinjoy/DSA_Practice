import sys
input = sys.stdin.readline

N,M = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))
used = [False]*N

def dfs(depth,current):
  if depth == M:
    print(' '.join(map(str,current)))
    return

  last = -1
  for i in range(0,N):
    if arr[i] != last:
      dfs(depth+1,current+[arr[i]])
      last = arr[i]
      
arr.sort()
dfs(0,[])