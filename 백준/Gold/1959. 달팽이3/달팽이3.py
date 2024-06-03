import sys
input = sys.stdin.readline

X,Y = map(int,input().split(' '))

K = 0
while True:
  if X-2*K <=2 or Y-2*K <= 2:
    break
  K += 1

result = 0
x,y = 0,0
if X>Y: # 세로가 가로보다 클 때
  result = 3 + 2*(Y-2)
  if Y%2 == 0 : # 가로가 짝수일 때
    x,y = 2+K,1+K
  else: # 가로가 홀수일 때
    x,y = X-K,Y-K
else: # 세로가 가로보다 작거나 같을 때
  result = 2*(X-1)
  if X%2 == 0 : # 세로가 짝수일 때
    x,y = X-K,1+K
  else: # 세로가 홀수일 때
    x,y = X-K,Y-K

print(result)
print(x,y)