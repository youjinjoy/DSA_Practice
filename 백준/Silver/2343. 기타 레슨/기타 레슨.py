import sys
input=sys.stdin.readline

n,m=map(int,input().split())
lecture_times=list(map(int,input().split()))

left=max(lecture_times)
right=sum(lecture_times)
answer=0

while left<right:
    cnt=1
    total=0
    mid=(left+right)//2

    for i in range(n):
        if total+lecture_times[i]>mid:
            total=lecture_times[i]
            cnt+=1
        else:
            total+=lecture_times[i]

    if cnt>m:
        left=mid+1
    else:
        right=mid

print(left)