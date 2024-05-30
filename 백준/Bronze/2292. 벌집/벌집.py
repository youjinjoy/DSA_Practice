import sys
input = sys.stdin.readline

n = int(input()) - 1
k = 1
while n>0:
  n -= 6*k
  k += 1
print(k)