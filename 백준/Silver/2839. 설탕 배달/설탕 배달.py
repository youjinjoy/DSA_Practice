import sys
input = sys.stdin.readline

N = int(input())

if N>5:
  a = [5000]*(N+1)
else:
  a = [5000]*6

a[3] = 1
a[5] = 1
for i in range(6,N+1):    
  a[i] = min(a[i-3],a[i-5]) + 1

if a[N] >= 5000:
  print(-1)
else:
  print(a[N])
