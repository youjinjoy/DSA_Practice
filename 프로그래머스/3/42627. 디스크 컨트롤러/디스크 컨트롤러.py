import heapq as hq

def solution(jobs):
    heap = []
    count = 0
    answer = 0
    b= -1
    
    jobs.sort()
    time = jobs[0][0]
    b = time-1
    while count < len(jobs):
        for s,t in jobs:
            if b < s <= time:
                hq.heappush(heap, [t,s])
        if heap:
            count += 1
            [t,s] = hq.heappop(heap)
            b = time
            time += t
            answer += time - s
        else:
            time += 1
    return answer//len(jobs)