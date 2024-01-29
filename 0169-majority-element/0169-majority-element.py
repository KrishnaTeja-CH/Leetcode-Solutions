class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Time - O(n*logn)
        #nums.sort()
        #return nums[len(nums)//2]

        # O(n)
        count = sol = 0
        for i in nums:
            if count == 0:
                sol = i
            count += 1 if i==sol else -1
        return sol