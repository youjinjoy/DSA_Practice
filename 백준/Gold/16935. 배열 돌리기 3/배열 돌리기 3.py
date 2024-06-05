import sys
input = sys.stdin.readline

height,width,R = map(int,input().split(' '))

A = [list(map(int,input().split(' '))) for _ in range(height)]

operation = list(map(int,input().split(' ')))

def measure(arr):
  height = len(arr)
  width = len(arr[0])
  height_half = height//2
  width_half = width//2
  return (height,width,height_half,width_half)

def op_1(arr):
  return arr[::-1]

def op_2(arr):
  temp = []
  for row in arr:
      temp.append(row[::-1])
  return temp

def op_3(arr):
  height,width,_,_ = measure(arr)
  temp = [[0 for _ in range(height)] for _ in range(width)]
  for i in range(0,width):
    for j in range(0,height):
      temp[i][j] = arr[height-(j+1)][i]
  return temp

def op_4(arr):
  height,width,_,_ = measure(arr)
  temp = [[0 for _ in range(height)] for _ in range(width)]
  for i in range(0,width):
    for j in range(0,height):
      temp[i][j] = arr[j][width-(i+1)]
  return temp

def op_5(arr):
  height,width,height_half,width_half = measure(arr)
  temp = [[0 for _ in range(width)]for _ in range(height)]
  for i in range(0,height_half):
    for j in range(0,width_half):
      temp[i][j] = arr[i+height_half][j]       
      temp[i][j+width_half] = arr[i][j]       
      temp[i+height_half][j+width_half] = arr[i][j+width_half]       
      temp[i+height_half][j] = arr[i+height_half][j+width_half]
  return temp

def op_6(arr):
  height,width,height_half,width_half = measure(arr)
  temp = [[0 for _ in range(width)]for _ in range(height)]
  for i in range(0,height_half):
    for j in range(0,width_half):
      temp[i][j] = arr[i][j+width_half]       
      temp[i][j+width_half] = arr[i+height_half][j+width_half]       
      temp[i+height_half][j+width_half] = arr[i+height_half][j]       
      temp[i+height_half][j] = arr[i][j]
  return temp

for op in operation:
  if op == 1:
    A = op_1(A)
  elif op == 2:
    A = op_2(A)
  elif op == 3:
    A = op_3(A)
  elif op == 4:
    A = op_4(A)
  elif op == 5:
    A = op_5(A)
  elif op == 6:
    A = op_6(A)

for row in A:
  print(' '.join(map(str,row)))