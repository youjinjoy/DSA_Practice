import sys
input = sys.stdin.readline

N,M,x,y,K = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(N)]
operations = list(map(int, input().split(' ')))

ewns = [(0,1),(0,-1),(-1,0),(1,0)] # 동 서 북 남

# 밑면 기준. X.
bottom = [
  None,
  # E W N S 순
  [3,4,5,2], # 밑이 1인 경우
  [3,4,1,6], # 밑이 2인 경우
  [1,6,2,5], # 밑이 3인 경우
  [6,1,2,5], # 밑이 4인 경우
  [3,4,6,1], # 밑이 5인 경우
  [3,4,2,5], # 밑이 6인 경우
]

# 1: 위, 2: 뒤, 3: 앞, 4: 왼쪽, 5: 오른쪽, 6: 밑
dice = [0 for _ in range(7)]

for op in operations:
  dx,dy = ewns[op-1]
  nx,ny = x+dx,y+dy
  if 0<=nx<N and 0<=ny<M:
    
    # 1: 위, 2: 뒤, 3: 앞, 4: 왼쪽, 5: 오른쪽, 6: 밑
    if op == 1:
      # 동쪽
      dice[1],dice[3],dice[6],dice[4] = dice[4],dice[1],dice[3],dice[6]
    elif op == 2:
      # 서쪽
      dice[1],dice[3],dice[6],dice[4] = dice[3],dice[6],dice[4],dice[1]
    elif op == 3:
      # 북쪽
      dice[6],dice[2],dice[1],dice[5] = dice[2],dice[1],dice[5],dice[6]
    else: # op ==4:
      # 남쪽
      dice[6],dice[2],dice[1],dice[5] = dice[5],dice[6],dice[2],dice[1]

    if maps[nx][ny] == 0:
      maps[nx][ny] = dice[6]
    else:
      dice[6] = maps[nx][ny]
      maps[nx][ny] = 0

    x,y = nx,ny
    print(dice[1])