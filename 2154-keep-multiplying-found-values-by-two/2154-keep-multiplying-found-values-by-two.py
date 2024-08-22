class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = set(nums)
        while original in n:
            original *= 2
        return original
        