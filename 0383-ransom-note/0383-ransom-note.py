class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        sol = Counter(ransomNote)
        res = Counter(magazine)
        for k in sol:
            res[k] = res.get(k, 0) - sol[k]
            if res[k] < 0:
                return False
        return True