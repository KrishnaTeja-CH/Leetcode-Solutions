class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()
        for i in range(len(nums)):
            j, k  = i + 1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0: k -= 1
                elif s < 0: j += 1
                else:
                    sol.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return sol