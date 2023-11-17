class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini = sys.maxsize
        total = l = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                total -= nums[l]
                mini = min(mini, i-l+1)
                l += 1
        return 0 if mini == sys.maxsize else mini
        