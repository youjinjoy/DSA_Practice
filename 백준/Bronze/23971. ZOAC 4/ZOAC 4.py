import sys
input = sys.stdin.readline

H,W,N,M = map(int,input().split(' '))
answer = 0
h = (N+1)
w = (M+1)

sero = H//h
if H%h != 0:
  sero += 1

garo = W//w
if W%w != 0:
  garo += 1
  
print(sero*garo)