import sys
input = sys.stdin.readline

N = int(input())

numbers = [0 for _ in range(10001)]
for _ in range(N):
  numbers[int(input())] += 1

for i in range(1,10001):
  n = numbers[i]
  while n > 0:
    print(i)
    n -= 1