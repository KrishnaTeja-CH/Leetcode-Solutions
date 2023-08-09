class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = s.split()
        return len(k[-1])
    