class Solution:
    def isArmstrong(self, n: int) -> bool:
        res = [int(i) for i in str(n)]
        sol = 0
        for i in res:
            sol += i**len(res)
        return sol == n