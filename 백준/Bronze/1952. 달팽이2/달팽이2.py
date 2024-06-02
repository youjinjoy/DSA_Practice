import sys
input = sys.stdin.readline

N,M = map(int,input().split(' '))

moves = [(0,1),(1,0),(0,-1),(-1,0)] # 시계 방향: 오른쪽, 아래, 왼쪽, 위

total = 1
answer = 0
i = 0
current = [0,0]
visited = [[False for _ in range(M)] for _ in range(N)]
while True:
  if total == N*M:
    break
  x,y = current
  visited[x][y] = True

  dx,dy = moves[i]
  nx,ny = x+dx,y+dy
  if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
    current[0],current[1] = nx,ny
  else:
    i = (i+1)%4
    dx,dy = moves[i]
    nx,ny = x+dx,y+dy
    current[0],current[1] = nx,ny
    answer += 1
  total += 1

print(answer)