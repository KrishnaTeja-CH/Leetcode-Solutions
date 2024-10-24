class Solution:
    def isArmstrong(self, n: int) -> bool:
        sol = [int(i) for i in str(n)]
        res = 0
        for i in sol:
            res += (i)**len(sol)
        return res==n
            
        