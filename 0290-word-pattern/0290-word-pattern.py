class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sol, res = [], []
        words = s.split(' ')
        for i in pattern:
            sol.append(pattern.index(i))
        for j in words:
            res.append(words.index(j))
        return sol == res
        

            