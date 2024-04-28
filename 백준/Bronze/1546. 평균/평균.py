import sys
input=sys.stdin

N=int(input.readline())
avg=list(map(int,input.readline().split(' ')))

m=max(avg)
answer=0
for n in avg:
  answer+=(n/m)*100

print(round(answer/N,2))