import sys
input = sys.stdin.readline

[M,N,L] = map(int,input().split(' '))
hunters = list(map(int,input().split(' ')))
hunters.sort()

count = 0
for _ in range(N):
  [x,y] = map(int,input().split(' '))
  left = 0
  right = len(hunters)-1
  while left <= right:
    mid = (left+right)//2

    if abs(hunters[mid]-x)+y <= L:
      count += 1
      break
    
    if x<=hunters[mid]:
      right = mid-1
    else:
      left = mid+1

print(count)
    