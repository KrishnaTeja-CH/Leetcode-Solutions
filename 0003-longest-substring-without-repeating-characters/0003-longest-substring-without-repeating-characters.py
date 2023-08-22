class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol = set()
        l = res = 0
        for i in range(len(s)):
            while s[i] in sol:
                sol.remove(s[l])
                l += 1
            sol.add(s[i])
            res = max(res, i-l+1)
        return res
        