class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
#Approach - 1
        ''' nums.reverse()
            nums[:k] = reversed(nums[:k])
            nums[k:] = reversed(nums[k:]) '''
#Approach -2 
        nums[:] = nums[-k:] + nums[:-k]
#Approach -3 
       # nums[k:] , nums[:k] = nums[:-k], nums[-k:]
        
        

     