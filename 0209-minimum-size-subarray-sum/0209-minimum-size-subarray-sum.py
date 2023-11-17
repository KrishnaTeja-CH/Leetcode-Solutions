class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = sys.maxsize
        total, l = 0, 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                res = min(res, i-l+1)
                total -= nums[l]
                l += 1
        return 0 if res == sys.maxsize else res                
        