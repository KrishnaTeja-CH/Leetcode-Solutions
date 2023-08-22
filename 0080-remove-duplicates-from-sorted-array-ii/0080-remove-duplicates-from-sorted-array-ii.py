class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums)-1 :
            if nums[i-1] == nums[i+1]:
                del nums[i]
            else:
                i += 1 
        