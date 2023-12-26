class Solution:
    def reverse(self, x: int) -> int:
        sign_value = -1 if -x > 0 else 1
        x = str(sign_value * x)[::-1]
        x = sign_value * int(x)
        if x > 2**31 -1 or x < -2**31:
            return 0
        else:
            return x
        