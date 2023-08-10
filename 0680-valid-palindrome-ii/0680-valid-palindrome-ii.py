class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        if s == s[::-1]: return True
        while i < j:
            if s[i] != s[j]:
                left = s[i+1 : j+1]
                right = s[i:j]
                if left == left[::-1] or right == right[::-1]:
                    return True
                else:
                    return False
            else:
                i += 1
                j -= 1
        return True