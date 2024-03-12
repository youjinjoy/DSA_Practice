import sys
input=sys.stdin.readline

n=int(input())
k=int(input())

sensors=list(map(int,input().split()))
sensors.sort()

gaps=[0]*(n-1)

for i in range(n-1):
  gaps[i]=sensors[i+1]-sensors[i]

gaps.sort()
print(sum(gaps[:n-k]))