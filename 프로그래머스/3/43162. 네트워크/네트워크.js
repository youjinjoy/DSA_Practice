function solution(n, computers) {
    const visited = Array(n).fill(false);
    
    const dfs = (node) => {
        if (visited[node]) return 0;
        visited[node]=true;

        for (let next=0 ; next<n ; next++){
            if (computers[node][next]){
                dfs(next);
                // visited[next]=true;
            }
        }
        return 1;
    }
    
    let cnt = 0;
    
    // [1 1 0] (0,0) (0,1)
    // [1 1 1] (1,0) (1,1) (1,2)
    // [0 1 1]       (2,1) (2,2)

    for (let i=0 ; i<n ; i++){
        cnt += dfs(i);
    }
    
    return cnt;
}