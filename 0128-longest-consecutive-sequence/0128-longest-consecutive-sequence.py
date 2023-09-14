class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums= set(nums)
        sol = res = 0
        for i in nums:
            if i-1 not in nums:
                sol = 1
                while i+1 in nums:
                    sol += 1
                    i += 1
                res = max(res, sol)
        return res
    
                
            
            
        
        
                
        