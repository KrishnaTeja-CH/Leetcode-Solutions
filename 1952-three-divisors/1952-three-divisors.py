class Solution:
    def isThree(self, n: int) -> bool:
        res = 0
        for i in range(1, n+1):
            if n<3: return False
            if n%i == 0: res += 1
        return res == 3