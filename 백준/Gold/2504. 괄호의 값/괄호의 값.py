import sys
input = sys.stdin.readline

def solution():
    bracket=input().strip()
    stack = []
    numbers = []
    for i in bracket:
        ## 여는 기호일 때
        if i == '(' or i == '[':
            stack.append(i)
        ## 닫는 기호일 때
        # )
        elif i == ')':
            while True:
                if not stack:
                    return 0
                x = stack.pop()
                if x=='[':
                    return 0
                elif x == '(':
                    if numbers:
                        stack.append(sum(numbers)*2)
                        numbers = []
                    else: # number = []
                        stack.append(2)
                    break
                else: # x가 숫자면
                    numbers.append(x)
        # ]
        elif i == ']':
            while True:
                if not stack:
                    return 0
                x = stack.pop()
                if x=='(':
                    return 0
                elif x == '[':
                    if numbers:
                        stack.append(sum(numbers)*3)
                        numbers = []
                    else: # numbers = []
                        stack.append(3)
                    break
                else: # x가 숫자면
                    numbers.append(x)

    answer = 0
    for s in stack:
        if type(s) == int:
            answer+=s
        else:
            return 0
    return answer

print(solution())