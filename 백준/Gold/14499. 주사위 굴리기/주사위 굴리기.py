import sys
input = sys.stdin.readline

N,M,x,y,K = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(N)]
operations = list(map(int, input().split(' ')))

dK = [None,(0,1),(0,-1),(-1,0),(1,0)] # 동 서 북 남

T = 0
B = 0
side = [None, 0, 0, 0, 0]
# 1: 왼쪽, 2: 오른쪽, 3: 앞, 4: 뒤

for op in operations:
  nx,ny = x+dK[op][0],y+dK[op][1]
  if nx in (-1,N):
    continue
  if ny in (-1,M):
    continue

  aux = op+1 if op%2 == 1 else op-1
  T,B,side[op],side[aux] = side[op],side[aux],B,T
  print(T)

  if maps[nx][ny] == 0:
    maps[nx][ny] = B
  else:
    B = maps[nx][ny]
    maps[nx][ny] = 0

  x,y = x+dK[op][0], y+dK[op][1]