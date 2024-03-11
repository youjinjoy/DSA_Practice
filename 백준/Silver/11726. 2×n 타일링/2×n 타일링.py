import sys
input=sys.stdin.readline

n=int(input())
a=[0 for _ in range(n+1)]
a[0]=0
a[1]=1
if n>1:
  a[2]=2

for i in range(3,n+1):
  a[i]=(a[i-1]+a[i-2])%10007

print(a[n])