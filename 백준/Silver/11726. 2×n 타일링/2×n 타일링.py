import sys
input = sys.stdin.readline

n = int(input())
# 필요한 최근 두 값을 저장합니다.
prev, current = 0, 1

for i in range(1, n + 1):
    prev, current = current, (prev + current) % 10007

print(current)
