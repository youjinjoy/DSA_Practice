def solution(rows, columns, queries):
    answer = []
    
    # 행렬 만들기
    maps = [[0 for _ in range(columns+1)]]
    maps += [[i*columns + j for j in range(columns+1)] for i in range(rows)]
    for i in range(rows+1):
        maps[i][0] = 0
    
    # 회전 적용
    for query in queries:
        x1,y1,x2,y2 = query
        arr = []
        for j in range(y1,y2):
            arr.append(maps[x1][j])
        for i in range(x1,x2):
            arr.append(maps[i][y2])
        for j in range(y2,y1,-1):
            arr.append(maps[x2][j])
        for i in range(x2,x1,-1):
            arr.append(maps[i][y1])
        answer.append(min(arr))
        new_arr = [arr[-1]]+arr[:-1]

        k=0
        for j in range(y1,y2):
            maps[x1][j] = new_arr[k]
            k += 1
        for i in range(x1,x2):
            maps[i][y2] = new_arr[k]
            k += 1
        for j in range(y2,y1,-1):
            maps[x2][j] = new_arr[k]
            k += 1
        for i in range(x2,x1,-1):
            maps[i][y1] = new_arr[k]
            k += 1
        
    return answer