import sys
input = sys.stdin.readline

X,Y = map(int,input().split(' '))

K = 0
left = 0
right = 2_100_000_001

while left<=right:
  mid = (left+right)//2
  sx,sy = X-2*mid, Y-2*mid
  
  if sx >2 and sy >2:
    left = mid+1
  elif sx<=0 or sy<=0:
    right = mid-1
  else:
    break
K = mid

result = 0
x,y = 0,0
if X>Y: # 세로가 가로보다 클 때
  result = 3 + 2*(Y-2)
  if Y%2 == 0 : # 가로가 짝수일 때
    x,y = 2+K,1+K
  else: # 가로가 홀수일 때
    x,y = X-K,Y-K
else: # 가로가 세로보다 작거나 클 때
  result = 2*(X-1)
  if X%2 == 0 : # 세로가 짝수일 때
    x,y = X-K,1+K
  else: # 세로가 홀수일 때
    x,y = X-K,Y-K

print(result)
print(x,y)