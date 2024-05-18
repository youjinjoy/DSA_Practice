import sys
input = sys.stdin.readline

[N,X] = map(int,input().split(' '))
A = list(map(int,input().split(' ')))

answer=''
for a in A:
  if a<X:
    answer += f'{a} '

print(answer)