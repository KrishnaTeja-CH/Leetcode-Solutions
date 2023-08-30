class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Forward
        pos = 0
        for i, n in enumerate(nums):
            if i > pos:
                return False
            pos = max(pos, i+n)
        return True

#Greedy - Backward

#       pos = len(nums)-1
#        for i in range(pos, -1, -1):
#            if i + nums[i] >= pos:
#                pos = i
#        return pos == 0 

            