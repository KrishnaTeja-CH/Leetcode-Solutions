class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = post = 1
        sol = [1]* len(nums)
        for i in range(len(nums)):
            sol[i] = pre
            pre *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            sol[i] *= post
            post *= nums[i]
        return sol