class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        sol = 0
        for i in range(len(s)):
            if len(set(s[i:i+3])) == 3:
                sol += 1
        return sol
                