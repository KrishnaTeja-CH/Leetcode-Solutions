class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        sol = float('inf')
        for i in nums:
            if abs(i) < abs(sol) or (abs(i)==abs(sol) and i>sol): sol = i
        return sol
        