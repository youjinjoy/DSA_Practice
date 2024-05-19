import sys
input = sys.stdin.readline

[row, column] = map(int,input().split(' '))
n = int(input())

rows = [row]
columns = [column]
for _ in range(n):
  [rc, l] = map(int,input().split(' '))
  if rc == 0:
    columns.append(l)
  else:
    rows.append(l)

rows.sort()
columns.sort()

lr = len(rows)-1
lc = len(columns)-1

max_r = 0
max_c = 0
for i in range(lr,0,-1):
  max_r = max(max_r, rows[i]-rows[i-1])
for i in range(lc,0,-1):
  max_c = max(max_c, columns[i]-columns[i-1])

max_r = max(max_r,rows[0])
max_c = max(max_c,columns[0])

print(max_r*max_c)