import sys
input = sys.stdin.readline

N = int(input())

a = [0 for _ in range(11)] # n은 11보다 작은 양수
a[1] = 1
a[2] = 2
a[3] = 4
for i in range(4,11):
    a[i] = a[i-1] + a[i-2] + a[i-3]

for _ in range(N):
    n = int(input())
    print(a[n])