class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n1, n2 = 0, sum(nums)
        for i in range(len(nums)):
            n2 -= nums[i]
            if n1 == n2: return i
            n1 += nums[i]
        return -1

            