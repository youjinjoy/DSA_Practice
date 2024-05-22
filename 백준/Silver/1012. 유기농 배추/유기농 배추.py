import sys
input = sys.stdin.readline

T = int(input())
dx = 1
dy = 1
for _ in range(T):
  [M,N,K] = map(int,input().split(' ')) # M: 가로, N: 세로

  farm = [[0 for _ in range(M)] for _ in range(N)]
  visited = [[False for _ in range(M)] for _ in range(N)]

  for _ in range(K):
    [x,y] = map(int,input().split(' '))
    farm[y][x] = 1
  
  count = 0 
  for i in range(N):
    for j in range(M):
        if farm[i][j] == 1 and not visited[i][j]:
          stack = [[i,j]]
          while stack:
            [A,B]=stack.pop()
            visited[A][B] = True
            for d in [[1,0],[-1,0],[0,1],[0,-1]]:
              a=A+d[0]
              b=B+d[1]
              if 0<=a<N and 0<=b<M and not visited[a][b] and farm[a][b] == 1:
                stack.append([a,b])
          count += 1

  print(count)