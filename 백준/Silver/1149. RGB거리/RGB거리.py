import sys
input = sys.stdin.readline

N = int(input())

r,g,b = 0,1,2
color = []
for _ in range(N):
  color.append(list(map(int,input().split(' '))))

a = [[0,0,0] for _ in range(N)]

a[0] = color[0]
a[1][r] = min(color[1][r]+a[0][g],color[1][r]+a[0][b])
a[1][g] = min(color[1][g]+a[0][r],color[1][g]+a[0][b])
a[1][b] = min(color[1][b]+a[0][r],color[1][b]+a[0][g])

for k in range(2,N):
  a[k][r] = min(color[k][r]+a[k-1][g],color[k][r]+a[k-1][b])
  a[k][g] = min(color[k][g]+a[k-1][r],color[k][g]+a[k-1][b])
  a[k][b] = min(color[k][b]+a[k-1][r],color[k][b]+a[k-1][g])

print(min(a[N-1]))