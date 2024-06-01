import sys
input = sys.stdin.readline

N = int(input())
maps = [list(map(int,input().strip())) for _ in range(N)]

def f(k,x,y):
  if k == 1:
    return str(maps[x][y])
  
  sk = k//2
  c = ''
  result = 0
  for i in range(x,x+k):
    for j in range(y,y+k):
      result += maps[i][j]
  if result == 0:
    c += '0'
  elif result == k*k:
    c += '1'
  else:
    c += f(sk,x,y)
    c += f(sk,x,y+sk)
    c += f(sk,x+sk,y)
    c += f(sk,x+sk,y+sk)
    c = '(' + c + ')'
  return c

print(f(N,0,0))