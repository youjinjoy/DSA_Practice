import sys
input = sys.stdin.readline


def solution():
  N = int(input())

  if N<100:
    return N

  answer = 99  
  for x in range(1,10):
    for i in range(-4,5):
      if 0 <= x+2*i < 10:
        h = x*100 + (x+i)*10 + x+2*i
        if h > N:
          return answer
        else:
          answer += 1

  return answer

print(solution())