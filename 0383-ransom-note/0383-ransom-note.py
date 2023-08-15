class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        sol, res = {}, {}
        for i in ransomNote:
            sol[i] = sol.get(i, 0) + 1
        for j in magazine:
            res[j] = res.get(j, 0) + 1
        for k in sol:
            res[k] = res.get(k, 0) - sol[k]
            if res[k] < 0:
                return False
        return True