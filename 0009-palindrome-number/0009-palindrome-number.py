class Solution:
    def isPalindrome(self, x: int) -> bool:
        original, reverse = x, 0
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x //= 10
        return original == reverse
