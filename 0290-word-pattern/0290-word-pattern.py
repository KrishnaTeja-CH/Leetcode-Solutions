class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words= s.split(' ')
        sol, res =[], []
        for i in pattern:
            sol.append(pattern.index(i))
        
        for j in words:
            res.append(words.index(j))    
        return res == sol
       
       
            