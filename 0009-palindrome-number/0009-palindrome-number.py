class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = [x for x in str(x)]
        return res==res[::-1]