import sys
input=sys.stdin.readline

string=input().strip()
m=int(input())

# stack1에 string의 문자 각각을 리스트로
stack1=list(string)
stack2=list()

for _ in range(m):
  command=input().strip()
  if command=='L' and stack1:
    word_1to2=stack1.pop()
    stack2.append(word_1to2)
  elif command=='D' and stack2:
    word_2to1=stack2.pop()
    stack1.append(word_2to1)
  elif command=='B' and stack1:
    stack1.pop()
  elif command[0]=='P':
    new_word=command[2]
    stack1.append(new_word)

# stack1 내용 문자열로 출력
print(''.join(stack1), end='')
# stack2 내용 문자열로 출력
print(''.join(reversed(stack2)), end='')