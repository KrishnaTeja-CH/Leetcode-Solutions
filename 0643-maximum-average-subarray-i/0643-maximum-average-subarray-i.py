class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k])
        maxi = curr
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            maxi = max(curr, maxi)
        return maxi/k
        