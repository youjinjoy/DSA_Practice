function solution(land) {
    var answer = 0;
    
    const rowLen = land[0].length;
    const colLen = land.length;
    // 석유 총량 및 행 기록
    // {
    //     1: [8],
    //     2: [8],
    //     3: [8],
    //     4: [7],
    //     ...
    //     7: [7, 2]
    // }
    const visited = Array(colLen).fill().map(() => Array(rowLen).fill(false));
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    const result = new Map();
    
    function dfs(start) {
        // 1이면 상하좌우 이동 (충돌 시 미이동. 이미 방문 시 미이동.)
        const stack = [start];
        const rowSet = new Set();
        let maxValue = 0;
        
        while (stack.length) {
            
            const [cx, cy] = stack.pop();
            if (!visited[cx][cy]) {
                maxValue++;
                rowSet.add(cy+1);
                visited[cx][cy] = true;
                for (let i = 0 ; i < 4 ; i++) {
                    const [nx, ny] = [cx + dx[i], cy + dy[i]];
                    if (nx >= 0 && nx < colLen && ny >= 0 && ny < rowLen && land[nx][ny] === 1 && !visited[nx][ny]) {
                        stack.push([nx,ny]);
                    }
                }
            }
        }

        for (let row of rowSet) {
            const R = result.get(row);
            if (!R) {
                result.set(row, maxValue);
            }
            else {
                result.set(row, R + maxValue);
            }
        }
        
    }
    
    for (let i = 0 ; i < colLen ; i++) {
        for (let j = 0 ; j < rowLen ; j++) {
            if (!visited[i][j] && land[i][j] === 1) {
                dfs([i,j]);
            }
        }
    }
    
    return Math.max(...result.values());
}