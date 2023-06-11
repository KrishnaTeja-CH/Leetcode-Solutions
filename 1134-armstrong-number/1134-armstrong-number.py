class Solution:
    def isArmstrong(self, n: int) -> bool:
        res = [int(i) for i in str(n)]
        sol = 0
        exp = len(res)
        for i in res:
            sol += i**exp
        return sol == n