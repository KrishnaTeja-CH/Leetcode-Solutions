class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, pos = 0, len(nums) - 1, len(nums) - 1
        ans = [0] * len(nums)  
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[pos] = nums[left] ** 2
                left += 1
            else:
                ans[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
            
        return ans
                    

        