class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in sol:
                return [i, sol[k]]
            sol[nums[i]] = i