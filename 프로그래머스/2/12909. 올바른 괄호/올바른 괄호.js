function solution(s){
    var answer = true;
    var stack = [];
    
    for (let token of s){
        if (token==='('){
            stack.push(token)
        }
        else{
            if (stack.length===0){
                answer = false;
                break;
            }
            stack.pop();
        }
    }
    
    if (stack.length !==0){
        answer=false;
    }

    return answer;
}