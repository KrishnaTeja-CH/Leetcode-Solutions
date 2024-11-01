class Solution:
    def reverse(self, x: int) -> int:
        sol = -1 if x < 0 else 1
        x = sol * int(str(abs(x))[::-1])
        return x if -2**31 <= x <=  2**31 - 1 else 0       