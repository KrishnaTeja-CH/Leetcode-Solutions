class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        sol, res = {}, {}
        for i in s:
            sol[i] = sol.get(i,0) + 1
        for j in t:
            res[j] = res.get(j,0) + 1
        return res == sol