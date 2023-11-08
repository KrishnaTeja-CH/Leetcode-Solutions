class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = set()
        for i in range(len(nums)):
            first = nums[i]
            j = i+1
            k = len(nums)-1 
            while j < k:
                second = nums[j]
                third = nums[k]
                solution = first + second + third
                if solution > 0:
                    k -= 1
                elif solution < 0:
                    j += 1
                else:
                    sol.add((first, second, third))
                    j += 1
                    k -= 1
        return sol



                   