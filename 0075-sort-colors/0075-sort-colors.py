class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Selection Sort
        for i in range(len(nums)):
            minIndex = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        
        #Bubble Sort
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[j] <= nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j] 