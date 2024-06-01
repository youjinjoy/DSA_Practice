def solution(word):
    current = []
    vowels = ['A','E','I','O','U']
    cnt = [0]
    
    def dfs(depth):
        
        if ''.join(current) == word:
            return True
        
        if depth == 5:
            return False
        
        for i in range(5):
            current.append(vowels[i])
            cnt[0] += 1
            found = dfs(depth+1)
            if(found) : return True
            current.pop()
    dfs(0)
    
    return cnt[0]