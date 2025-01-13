function solution(msg) {
    const D = new Map();
    for (let i = 0 ; i < 26 ; i++) {
        const w = String.fromCharCode(65+i);
        D.set(w, i+1);
    }
    
    const answer = [];
    let i = 0;
    let w = '';
    let lastIndex = 27;
    while(i < msg.length) {
        c = msg[i];
        while(D.get(w+c)) {
            w += c;
            i += 1;
            c = msg[i];
        }
        answer.push(D.get(w));
        D.set(w+c, lastIndex);
        lastIndex += 1;
        w = '';
    }
    
    return answer;
}