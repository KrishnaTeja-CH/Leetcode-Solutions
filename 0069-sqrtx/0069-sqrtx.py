class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l<=r:
            m = (l+r)//2
            sol = m*m
            if sol == x:
                return m
            elif sol < x:
                l = m+1
            else:
                r = m-1
        return r     
        