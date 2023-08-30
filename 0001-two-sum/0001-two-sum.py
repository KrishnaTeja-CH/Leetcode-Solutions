class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in sol:
                return [sol[k], i]
            sol[nums[i]] = i