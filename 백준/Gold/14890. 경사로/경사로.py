import sys
input = sys.stdin.readline

N,L = map(int,input().split(' '))
maps = [list(map(int,input().split(' '))) for _ in range(N)]


# 오르막길 가능한지 탐색
def is_up_possible(flat):
  if flat >= L:
    return True
  else:
    return False

# 내리막길 가능한지 탐색
def is_down_possible_row(index,row):
  if index - 1 + L >= N:
    return False
  
  for next_index in range(index+1,index+L):
    if maps[row][index] == maps[row][next_index]:
      continue
    else:
      return False
  
  return True

# 내리막길 가능한지 탐색 (2)
def is_down_possible_col(index,col):
  if index - 1 + L >= N:
    return False
  
  for next_index in range(index+1,index+L):
    if maps[index][col] == maps[next_index][col]:
      continue
    else:
      return False
  
  return True


ans = 0
# 가로 길 탐색 ( → )
for row in range(N):
  flat = 1
  col = 1
  cross = True
  prev = maps[row][0]
  while col < N:
    cur = maps[row][col]
    if prev == cur:
      flat += 1
    elif prev + 1 == cur:
      if is_up_possible(flat):
        flat = 1
      else:
        cross = False
        break
    elif prev == cur + 1:
      if is_down_possible_row(col,row):
        flat = 0
        col += L-1
      else:
        cross = False
        break
    else:
      cross = False
      break
    prev = cur
    col += 1

  if cross:
    ans += 1

# 세로 길 탐색 ( ↓ )
for col in range(N):
  flat = 1
  row = 1
  cross = True
  prev = maps[0][col]
  while row < N:
    cur = maps[row][col]
    if prev == cur:
      flat += 1
    elif prev + 1 == cur:
      if is_up_possible(flat):
        flat = 1
      else:
        cross = False
        break
    elif prev == cur + 1:
      if is_down_possible_col(row,col):
        flat = 0
        row += L-1
      else:
        cross = False
        break
    else:
      cross = False
      break
    prev = cur
    row += 1

  if cross:
    ans += 1

print(ans)