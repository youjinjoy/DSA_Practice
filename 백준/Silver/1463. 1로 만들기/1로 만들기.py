import sys
input = sys.stdin.readline

N = int(input())

a = [float("inf")]*(N+1)

a[1] = 0
if N >= 2:
  a[2] = 1
if N >= 3:
  a[3] = 1

for i in range(4,N+1):
  if i%6 == 0:
    a[i] = min(a[i//3],a[i//2],a[i-1]) + 1
  elif i%3 == 0:
    a[i] = min(a[i//3],a[i-1]) + 1
  elif i%2 == 0:
    a[i] = min(a[i//2],a[i-1]) + 1
  else:
    a[i] = a[i-1] + 1

print(a[N])