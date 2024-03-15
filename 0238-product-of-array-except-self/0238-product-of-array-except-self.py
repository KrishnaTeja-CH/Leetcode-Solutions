class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = post = 1
        sol = [1] * n  
        for i in range(n):
            sol[i] = pre
            pre *= nums[i]  
        print(sol)
        for i in range(n-1,-1,-1):
            sol[i] *= post
            post *= nums[i]
        return sol
            