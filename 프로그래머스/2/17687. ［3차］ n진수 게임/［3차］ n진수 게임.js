function solution(n, t, m, p) {
    const D = new Map();
    for (let i = 0 ; i < 6 ; i++) {
        D.set(10+i, String.fromCharCode(65+i));
    }
        
    let answer = '';
    const result = [];
    for (let i = 2 ; i <= m * t ; i++) {
        
        const subResult =[];
        let number = i
        
        while (number >= n) {
            const remain = number % n;
            if (remain >= 10) {
                subResult.push(D.get(remain));
            }
            else {
                subResult.push(remain);
            }
            
            number = Math.floor(number/n);
        }
        if (number >= 10) {
            subResult.push(D.get(number));
        }
        else {
            subResult.push(number);        
        }
        result.push(...subResult.reverse());
    }
    
    const finalResult = [0,1].concat(result);
    for (let i = 0 ; i < t ; i++) {
        answer += finalResult[m*i + p - 1];
    }
    
    return answer;
}