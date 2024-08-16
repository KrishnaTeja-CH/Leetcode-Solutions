class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi, sol = float('-inf'), 0
        for i in range(len(nums)):
            sol += nums[i]
            maxi = max(maxi, sol)
            
            if sol<0:
                sol = 0
        return maxi
    
        