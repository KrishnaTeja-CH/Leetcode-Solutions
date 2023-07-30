class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sol = 0
        for i in range(k):
            sol += nums[i]
        maxSum = sol
        for i in range(k, len(nums)):
            sol += nums[i] - nums[i-k]
            maxSum = max(sol, maxSum)
        return maxSum/k