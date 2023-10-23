class Solution:
    def jump(self, nums: List[int]) -> int:
        pos, count = len(nums) - 1, 0
        while pos > 0:
            for i in range(pos):
                if i + nums[i] >= pos:
                    pos = i
                    count += 1
                    break
        return count