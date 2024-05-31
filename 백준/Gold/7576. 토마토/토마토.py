import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split(' '))

farm = [list(map(int,input().split(' '))) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

max = 0
q = deque()
for i in range(N):
  for j in range(M):
    if farm[i][j] == 1 and not visited[i][j]:
      visited[i][j] = True
      q.append((i,j,0))

while q:
  x,y,day = q.popleft()
  
  if day > max:
    max = day
  
  for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
    nx = x+dx
    ny = y+dy
    if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and farm[nx][ny] != -1:
      q.append((nx,ny,day+1))
      farm[nx][ny] = 1
      visited[nx][ny] = True

flag = True
for i in range(N):
  for j in range(M):
    if farm[i][j] == 0:
      flag = False

if flag:
  print(max)
else:
  print(-1)