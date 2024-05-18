import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
  S = input().strip()
  s=S.split('X')
  answer=0
  for o in s:
    l = len(o)
    answer += l*(l+1)/2
  print(int(answer))