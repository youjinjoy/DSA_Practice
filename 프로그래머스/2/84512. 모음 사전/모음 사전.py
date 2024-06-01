def solution(word):
    cnt = [0]
    
    def dfs(current):
        
        if current == word:
            return True
        
        if len(current) == 5:
            return False
        
        for c in "AEIOU":
            current += c
            cnt[0] += 1
            if dfs(current):
                return True
            current = current[:-1]
    dfs("")
    
    return cnt[0]