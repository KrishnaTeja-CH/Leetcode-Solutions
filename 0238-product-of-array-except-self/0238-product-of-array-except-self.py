class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R, Sol = [0] * n, [0] * n, [0] * n
        L[0], R[-1] = 1, 1
        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]
        for i in reversed(range(len(nums)-1)):
            R[i] = R[i+1] * nums[i+1]
        for i in range(len(nums)):
            Sol[i] = L[i] * R[i]
        return Sol
        
     
            
            
        