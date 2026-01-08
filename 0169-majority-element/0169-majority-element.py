class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sol = res = 0
        for i in nums:
            if sol == 0:
                res = i
            sol += 1 if i == res else -1
        return res
