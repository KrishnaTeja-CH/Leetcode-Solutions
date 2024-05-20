class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        for i in range(n+1):
            res += i if i%m!=0 else -i
        return res
        
        