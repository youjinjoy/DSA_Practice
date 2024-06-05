import sys
input = sys.stdin.readline

height,width,R = map(int,input().split(' '))

arr = [list(map(int,input().split(' '))) for _ in range(height)]

operation = list(map(int,input().split(' ')))

for op in operation:
  height = len(arr)
  width = len(arr[0])
  if op == 1:
    # for _ in range(R):
    for i in range(height//2):
      temp = arr[i]
      arr[i] = arr[height-(i+1)]
      arr[height-(i+1)] = temp
  elif op == 2:
    # for _ in range(R):
    for i in range(height):
      for j in range(width//2):
        temp = arr[i][j]
        arr[i][j] = arr[i][width-(j+1)]
        arr[i][width-(j+1)] = temp
  elif op == 3:
    # for _ in range(R):
    maps = []
    for j in range(len(arr[0])):
      column = []
      for i in range(len(arr)-1,-1,-1):
        column.append(arr[i][j])
      maps.append(column)
    arr = maps
  elif op == 4:
    # for _ in range(R):
    maps = []
    for j in range(len(arr[0])-1,-1,-1):
      row = []
      for i in range(0,len(arr)):
        row.append(arr[i][j])
      maps.append(row)
    arr = maps
  elif op == 5:
    # for _ in range(R):
    temp = []
    for i in range(0,height//2):
      temp.append(arr[i][0:width//2])
      for j in range(0,width//2):
        arr[i][j] = arr[i-height//2][j]
    for i in range(height//2,height):
      for j in range(width//2):
        arr[i][j] = arr[i][j+width//2]
    for i in range(height//2,height):
      for j in range(width//2,width):
        arr[i][j] = arr[i-height//2][j]
    for i in range(height//2):
      for j in range(width//2,width):
        arr[i][j] = temp[i][j-width//2]
  elif op == 6:
    # for _ in range(R):
    temp = []
    for i in range(0,height//2):
      temp.append(arr[i][0:width//2])
      for j in range(0,width//2):
        arr[i][j] = arr[i][j+width//2]
    for i in range(0,height//2):
      for j in range(width//2,width):
        arr[i][j] = arr[i+height//2][j]
    for i in range(height//2,height):
      for j in range(width//2,width):
        arr[i][j] = arr[i][j-width//2]
    for i in range(height//2,height):
      for j in range(width//2):
        arr[i][j] = temp[i-height//2][j]

for row in arr:
  print(' '.join(map(str,row)))