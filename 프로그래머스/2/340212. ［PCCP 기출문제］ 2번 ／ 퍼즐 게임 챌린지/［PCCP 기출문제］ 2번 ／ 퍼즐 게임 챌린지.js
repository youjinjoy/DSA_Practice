function solution(diffs, times, limit) {

    let answer = 1;

    
    const N = diffs.length;
    
    let left = 1;
    let right = diffs.reduce((acc, cur) => Math.max(acc, cur), 1);
    
    while(left <= right) {
        let mid = parseInt((left+right)/2);
        let totalTime = 0;

        for (let i = 0 ; i < N ; i++) {            
            const diff = diffs[i];
            const time_cur = times[i];
            
            if (diff <= mid) {
                totalTime += time_cur;
            }
            else {
                totalTime += (diff - mid + 1) * time_cur;
                if (i > 0) totalTime += (diff - mid) * times[i-1];
            }
            
            if (totalTime > limit) {
                break;
            }
        }
        
        if (totalTime > limit) {
            left = mid + 1;
            answer = left;
        }
        else {
            right = mid - 1;
        }
    }
    
    return answer;
}