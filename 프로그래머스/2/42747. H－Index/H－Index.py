def solution(citations):
    lc = len(citations)
    citations.sort()
    answer = 0
    for i in range(lc):
        if citations[i] >= lc-i:
            answer=lc-i
            break
    return answer