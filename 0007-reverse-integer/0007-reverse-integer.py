class Solution:
    def reverse(self, x: int) -> int:
        sign_value = -1 if x < 0 else 1
        x = sign_value * int(str(abs(x))[::-1])
        return x if -2**31 <= x <= 2**31 - 1 else 0
        