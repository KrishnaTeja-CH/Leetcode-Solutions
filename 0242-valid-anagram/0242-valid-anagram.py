class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        s = "".join(s)
        t = "".join(t)
        return t == s
        