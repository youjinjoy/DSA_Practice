import sys
import heapq as hq

input = sys.stdin.readline
N=int(input())


for _ in range(N):
    # 최소 힙, 최대 힙, 데이터 동기화용 딕셔너리 만들기
    minh = []
    maxh = []
    sync = {}

    T=int(input())
    operations = [input() for _ in range(T)]

    for operation in operations:
        [o,n]=operation.split(' ')
        n=int(n)        
        if o == 'I':    # Insert 시 최소, 최대 힙에 둘다 넣기
            hq.heappush(maxh, -n)
            hq.heappush(minh, n)
            sync[n] = sync.get(n,0)+1
        elif o == 'D':  # Delete 시 각 힙에서 빼기
            # 힙에서 뺄 때 sync 확인 후 아직 0이 아니면 -1
            if n == 1:
                while maxh:
                    target = -hq.heappop(maxh)
                    if sync[target] == 0:
                        continue
                    else:
                        sync[target] -= 1
                        break
            elif n == -1:
                while minh:
                    target = hq.heappop(minh)
                    if sync[target] == 0:
                        continue
                    else:
                        sync[target] -= 1
                        break

    # 데이터 동기화
    while minh and sync[minh[0]] == 0:
        hq.heappop(minh)
    while maxh and sync[-maxh[0]] == 0:
        hq.heappop(maxh)

    if maxh and minh:
        print(-maxh[0],minh[0])
    else:
        print('EMPTY')