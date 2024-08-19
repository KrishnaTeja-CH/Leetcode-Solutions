class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1   
        for _ in range(n):
            one, two = one+two, one
        return two 
        