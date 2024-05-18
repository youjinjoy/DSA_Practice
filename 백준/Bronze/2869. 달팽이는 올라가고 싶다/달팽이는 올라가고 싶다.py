import sys
input = sys.stdin.readline

[A,B,V] = list(map(int,input().split(' ')))

print((V-A)//(A-B)+2) if (V-A)%(A-B) else print((V-A)//(A-B)+1)