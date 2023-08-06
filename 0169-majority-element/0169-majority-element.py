class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time - O(n*logn)
        nums.sort()
        return nums[len(nums)//2]
                
        
        