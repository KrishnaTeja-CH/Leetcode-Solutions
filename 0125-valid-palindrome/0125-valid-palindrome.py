class Solution:
    def isPalindrome(self, s: str) -> bool:
        sol = [i for i in s.lower() if i.isalnum()]
        return sol==sol[::-1]
        