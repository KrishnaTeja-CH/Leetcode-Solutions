class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L, R, Sol = [0] * n, [0] * n, [0] * n
        L[0], R[-1] = 1, 1
        for i in range(1,n):
            L[i] = nums[i-1] * L[i-1]
        for i in reversed(range(n-1)):
            R[i] = nums[i+1] * R[i+1]
        for i in range(n):
            Sol[i] = L[i] * R[i]
        return Sol
            
            
        