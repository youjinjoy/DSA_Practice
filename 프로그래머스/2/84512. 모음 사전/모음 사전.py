def solution(word):
    cnt = [0]
    
    def dfs(current):
        
        if current == word:
            return True
        
        if len(current) == 5:
            return False
        
        for c in "AEIOU":
            cnt[0] += 1
            if dfs(current+c):
                return True
    dfs("")
    
    return cnt[0]