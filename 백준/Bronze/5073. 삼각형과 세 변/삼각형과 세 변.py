import sys
input = sys.stdin.readline

def is_triangle(a,b,c):
  if a+b<=c or a+c<=b or b+c<=a:
    return False
  else:
    return True

while True:
  x,y,z = map(int,input().split(' '))
  if x+y+z == 0:
    break

  if is_triangle(x,y,z):
    if x==y==z:
      print("Equilateral")
    elif x==y or x==z or y==z:
      print("Isosceles")
    else:
      print("Scalene")
  else:
    print("Invalid")