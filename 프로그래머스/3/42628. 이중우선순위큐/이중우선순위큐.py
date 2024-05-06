import heapq as hq

def solution(operations):
    # 최소 힙, 최대 힙, deque 만들기
    minh = []
    maxh = []
    stack = []
    # Insert 시 0 기준으로 최소, 최대 힙에 넣기
    # Delete 시 각 힙에 맞게 빼기
    ### 한쪽 힙에 없는데 다른쪽 힙은 있으면 전부 deque에 넣고 구하기
    for operation in operations:
        [o,n]=operation.split(' ')
        n=int(n)
        
        if o == 'I':
            if n >= 0:
                hq.heappush(maxh,-n)
            else: # n < 0
                hq.heappush(minh,n)
        elif o == 'D':
            if n == 1 and maxh:
                hq.heappop(maxh)
            elif n == 1 and minh: # maxh는 비어있는 경우
                while minh:
                    stack.append(hq.heappop(minh))
                stack.pop()
                while stack:
                    hq.heappush(minh, stack.pop())
            elif n == -1 and minh:
                hq.heappop(minh)
            elif n == -1 and maxh: # minh는 비어있는 경우
                while maxh:
                    stack.append(hq.heappop(maxh))
                stack.pop()
                while stack:
                    hq.heappush(maxh, stack.pop())
    max_v=0
    min_v=0
    
    if minh and maxh:
        min_v = hq.heappop(minh)
        max_v = -hq.heappop(maxh)
    elif minh:
        min_v = minh[0]
        while minh:
            max_v = hq.heappop(minh)
    elif maxh:
        max_v = -maxh[0]
        while maxh:
            min_v = -hq.heappop(maxh)
    
    answer = [max_v, min_v]
    return answer