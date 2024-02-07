class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        for i in range(1, len(nums)):
            pre.append(pre[-1] + nums[i])
        return pre