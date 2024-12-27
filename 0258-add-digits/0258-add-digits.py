class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sol = 0
            while num:
                sol += num % 10
                num = num // 10
            num = sol
        return num
        