import sys
input = sys.stdin.readline

def solution():
    bracket=input().strip()
    stack = []
    # numbers 배열 없앤 버전
    
    for i in bracket:
        ## 여는 기호일 때
        if i == '(' or i == '[':
            stack.append(i)
        ## 닫는 기호일 때
        # )
        elif i == ')':
            temp = 0
            while True:
                if not stack:
                    return 0
                top = stack.pop()
                if top == '(':
                    if temp == 0:
                        stack.append(2)
                    else:
                        stack.append(2 * temp)
                    break
                elif top == '[':
                    return 0
                else: # top이 숫자일 때
                    temp += top
        # ]
        elif i == ']':
            temp = 0
            while True:
                if not stack:
                    return 0
                top = stack.pop()
                if top == '[':
                    if temp == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * temp)
                    break
                elif top == '(':
                    return 0
                else: # top이 숫자일 때
                    temp += top

    answer = 0
    for s in stack:
        if type(s) != int:
            return 0
        answer += s
    return answer

print(solution())