import sys
input = sys.stdin.readline

N,M = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))
used = [False]*N
history = []

def dfs(depth,current):
  if depth == M:
    current_string = ' '.join(map(str,current))
    if current_string not in history:
      print(current_string)
      history.append(current_string)
    return

  for i in range(N):
    if not used[i]:
      used[i] = True
      dfs(depth+1,current+[arr[i]])
      used[i] = False
      
arr.sort()
dfs(0,[])