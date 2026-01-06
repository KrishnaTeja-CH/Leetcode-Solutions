class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """ Sol-1 """
        move = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[move], nums[i] = nums[i], nums[move]
                move += 1



        
        """ Sol-2
        
        move = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                move += 1
            elif move > 0:
                temp = nums[i]
                nums[i] = 0
                nums[i-move] = temp
                
        """
        