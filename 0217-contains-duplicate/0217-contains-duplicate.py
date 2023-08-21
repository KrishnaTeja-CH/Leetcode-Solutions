class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i, j in enumerate(nums):
            if j in hm:
                return True
            hm[nums[i]] = j
        