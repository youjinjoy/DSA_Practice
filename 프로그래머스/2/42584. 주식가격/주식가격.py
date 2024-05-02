def solution(prices):
    stack = []
    time = [0 for _ in prices]
    n = len(time)
    
    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            time[j] = i-j
        stack.append(i)
        
    while stack:
        t = stack.pop()
        time[t] = n-t-1
            
    return time