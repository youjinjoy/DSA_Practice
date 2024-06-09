import sys
input = sys.stdin.readline

N,M,R = map(int, input().split(' '))

maps = [list(map(int,input().split(' '))) for _ in range(N)]
loops = min(N,M) // 2

def rotate(layer,r):
  total_elements = 2*(N-2*layer)+2*(M-2*layer)-4
  r = r % total_elements
  elements = []

  for i in range(layer,M-layer):
    elements.append(maps[layer][i])
  for i in range(layer+1,N-layer):
    elements.append(maps[i][M-layer-1])
  for i in range(M-layer-2,layer-1,-1):
    elements.append(maps[N-layer-1][i])
  for i in range(N-layer-2,layer,-1):
    elements.append(maps[i][layer])
  
  elements_rotated = elements[r:]+elements[:r]

  idx = 0
  for i in range(layer,M-layer):
    maps[layer][i] = elements_rotated[idx]
    idx += 1
  for i in range(layer+1,N-layer):
    maps[i][M-layer-1] = elements_rotated[idx]
    idx += 1
  for i in range(M-layer-2,layer-1,-1):
    maps[N-layer-1][i] = elements_rotated[idx]
    idx += 1
  for i in range(N-layer-2,layer,-1):
    maps[i][layer] = elements_rotated[idx]
    idx += 1

for layer in range(loops):
  rotate(layer,R)

for row in maps:
  print(' '.join(map(str,row)))