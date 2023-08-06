class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Time - O(n*logn)
        #nums.sort()
        #return nums[len(nums)//2]

        # O(n)
        count = sol = 0
        for i in nums:
            if count == 0: sol = i
            if i == sol: count += 1
            else: count -= 1
        return sol
                
        
        