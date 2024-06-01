import sys
input = sys.stdin.readline

N,M = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))
used = [False]*N

def dfs(depth,start,current):
  if depth == M:
    print(' '.join(map(str,current)))
    return

  last = -1
  for i in range(start,N):
    if arr[i] != last:
      dfs(depth+1,i,current+[arr[i]])
      last = arr[i]
      
arr.sort()
dfs(0,0,[])