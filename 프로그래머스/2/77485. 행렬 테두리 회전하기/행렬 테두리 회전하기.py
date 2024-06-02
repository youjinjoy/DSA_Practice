def solution(rows, columns, queries):
    answer = []
    
    # 행렬 만들기
    maps = [[i*columns + j + 1 for j in range(columns)] for i in range(rows)]
    
    # 회전 적용
    for x1,y1,x2,y2 in queries:
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1 # 인덱스 조정
        temp = maps[x1][y1]
        m = min(10000,temp)
        
        for i in range(x1,x2):
            maps[i][y1] = maps[i+1][y1]
            m = min(m, maps[i][y1])
            
        for j in range(y1,y2):
            maps[x2][j] = maps[x2][j+1]
            m = min(m, maps[x2][j])
            
        for i in range(x2,x1,-1):
            maps[i][y2] = maps[i-1][y2]
            m = min(m, maps[i][y2])
            
        for j in range(y2,y1,-1):
            maps[x1][j] = maps[x1][j-1]
            m = min(m, maps[x1][j])

        maps[x1][y1+1] = temp
        answer.append(m)
        
    return answer