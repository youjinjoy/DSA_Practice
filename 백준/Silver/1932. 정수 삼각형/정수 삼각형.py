import sys
input=sys.stdin.readline

n=int(input())

# n번 arr에 값 넣기 (2차원 배열. 삼각형 모양)
arr=[list(map(int,input().split())) for _ in range(n)]

a=[[0 for _ in range(i)] for i in range(1,n+1)]
a[0][0]=arr[0][0]
for i in range(1,n):
  for j in range(i+1):
    if j==0:
      a[i][j]=a[i-1][j]+arr[i][j]
    elif j==i:
      a[i][j]=a[i-1][j-1]+arr[i][j]
    else:
      a[i][j]=max(a[i-1][j-1],a[i-1][j])+arr[i][j]

print(max(a[n-1]))