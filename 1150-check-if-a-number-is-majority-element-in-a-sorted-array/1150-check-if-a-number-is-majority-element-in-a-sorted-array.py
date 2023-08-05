class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = 0
        num = 0
        for i in nums:
            if nums.count(i) > count:
                count = nums.count(i)
                num = i
        return (count > len(nums)/2 and num == target) 
          
    