class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output, l, r = [0] * n, [0] * n, [0] * n
        l[0], r[-1] = 1, 1
        for i in range(1, n):
            l[i] = l[i-1] * nums[i-1]
        for i in reversed(range(n-1)):
            r[i] = r[i+1] * nums[i+1]
        for i in range(n):
            output[i] = l[i] * r[i]            
        return output