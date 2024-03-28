function solution(numbers, target) {
    const depth = numbers.length;

    const dfs = (total,index) => {
        if (index === depth) {
            if (total === target) {
                return 1;
            }
            else{
                return 0;
            }
        }   
        
        return dfs(total+numbers[index],index+1)+dfs(total-numbers[index],index+1);
    }
    
    return dfs(numbers[0],1)+dfs(-numbers[0], 1)
}