function solution(cacheSize, cities) {
    if (cacheSize === 0) {
        return 5 * cities.length;
    }
    
    let answer = 0;
    const cache = [];
    
    for (let city of cities) {
        city = city.toLowerCase();
        const idx = cache.indexOf(city);
        
        if (idx > -1) {
            cache.splice(idx,1)
            cache.push(city);
            answer += 1;
        }
        else {
            if (cache.length >= cacheSize) {
                cache.shift();
            }
            cache.push(city);
            answer += 5;
        }
    }
    return answer;
}