class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1, s2, i = min(strs), max(strs), 0
        while i<len(s1):
            if s1[i] != s2[i]:
                s1 = s1[:i]
            i += 1
        return s1
            
        

        