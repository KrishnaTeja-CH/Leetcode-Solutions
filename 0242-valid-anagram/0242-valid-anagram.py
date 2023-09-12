class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sol, res = Counter(s), Counter(t)
       
        return res == sol