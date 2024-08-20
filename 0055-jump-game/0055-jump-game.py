class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas  = 0
        for i, j in enumerate(nums):
            if i > gas:
                return False
            gas = max(gas, i+j)
        return True

                
        