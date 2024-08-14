class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        sol = min([abs(i) for i in nums])
        return sol if sol in nums else -sol   