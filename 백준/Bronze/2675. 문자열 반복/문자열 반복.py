import sys

tc= int(sys.stdin.readline())

cases=[]
answer=''
for i in range(tc):
    n,string=sys.stdin.readline().split(' ')
    n=int(n)
    string=string.strip()
    for s in string:
        answer+=n*s
    answer+='\n'

print(answer)