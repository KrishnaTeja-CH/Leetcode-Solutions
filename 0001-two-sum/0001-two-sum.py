class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solmap = {}
        for i in range(len(nums)): 
            diff = target - nums[i] # i =0, nums[i]=2
            if diff in solmap: # diff = 7
                return [i, solmap[diff]]
            solmap[nums[i]] = i # 0:"2" for 1 iteration