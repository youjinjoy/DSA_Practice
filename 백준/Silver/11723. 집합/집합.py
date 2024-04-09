import sys
# sys.setrecursionlimit(10**9)
# sys.stdin=open("test.txt")

input=sys.stdin.readline
n=int(input())
s=0

while n:
    n-=1
    arr=input().split()
    if len(arr)>=2:
        inst=arr[0]
        x=int(arr[1])
    else:
        inst=arr[0]
        x=-1
    
    if inst=='add':
        s|=(1<<x)
    elif inst=='remove':
        s&=~(1<<x)
    elif inst=='check':
        ch = s&(1<<x)
        if ch==0:
            print(0)
        else:
            print(1)
    elif inst=='toggle':
        s^=(1<<x)
    elif inst=='all':
        s=int(bin(2**21-1)[2:],2)
        # print(s)
    elif inst=='empty':
        s=0