import sys

X,Y=list(map(str.strip, sys.stdin.readlines()))
lx=len(X)
ly=len(Y)
LCS=[[0 for _ in range(ly+1)] for _ in range(lx+1)]

for i in range(1,lx+1):
  for j in range(1,ly+1):
    if X[i-1]==Y[j-1]:
      LCS[i][j]=LCS[i-1][j-1]+1
    else:
      LCS[i][j]=max(LCS[i-1][j], LCS[i][j-1])

x=lx
y=ly
number=LCS[x][y]
string=[]
while (LCS[x][y]!=0):
  if LCS[x][y]==LCS[x-1][y]:
    x=x-1
  elif LCS[x][y]==LCS[x][y-1]:
    y=y-1
  else:
    string.append(X[x-1])
    x=x-1
    y=y-1

print(number)
print(''.join(reversed(string)))