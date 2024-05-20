import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

[N,r,c] = map(int,input().split(' '))

def f(i,j,k):
  if k == 1:
    if (i,j) == (0,0):
      return 0
    elif (i,j) == (0,1):
      return 1
    elif (i,j) == (1,0):
      return 2
    elif (i,j) == (1,1):
      return 3
    
  K_1=2**(k-1)
  K=2**k
  if 0 <= i < K_1 and 0 <= j < K_1:
    return f(i,j,k-1)
  elif 0 <= i < K_1 and K_1 <= j < K:
    return f(i,j-K_1,k-1)+2**(2*(k-1))
  elif K_1 <= i < K and 0 <= j < K_1:
    return f(i-K_1,j,k-1)+2*2**(2*(k-1))
  else: # K <= i < K and K <= j < K:
    return f(i-K_1,j-K_1,k-1)+3*2**(2*(k-1))
  
print(f(r,c,N))