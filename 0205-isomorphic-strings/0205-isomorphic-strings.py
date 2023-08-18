class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sol, res = [], []            
        for i in s:
            sol.append(s.index(i))
        for j in t:
            res.append(t.index(j))
        return sol == res