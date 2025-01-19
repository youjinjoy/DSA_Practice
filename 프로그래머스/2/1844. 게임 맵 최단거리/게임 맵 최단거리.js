function solution(maps) {
    let answer = -1;
    
    const n = maps.length;
    const m = maps[0].length;
    
    const visited = Array.from({length: n}, () => Array(m).fill(false));
          
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];
    
    const queue = [[0,0,1]];
    visited[0][0] = true;
    while (queue.length) {
        const [cx, cy, d] = queue.shift();
        
        for (let i = 0 ; i < 4 ; i++) {
            const [nx, ny] = [cx+dx[i], cy+dy[i]];
            
            if (nx === n-1 && ny === m-1) {
                return d + 1;
            }
            
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && maps[nx][ny] && !visited[nx][ny]) {
                visited[nx][ny] = true;
                queue.push([nx,ny, d+1]);
            }
        }
    }
    
    return answer;
}