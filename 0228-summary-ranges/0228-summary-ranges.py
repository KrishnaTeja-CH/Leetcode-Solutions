class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i,k = 0,[]
        while i < len(nums):
            res = nums[i]
            while i+1 < len(nums) and nums[i]+1 == nums[i+1]:
                i += 1
            if res != nums[i]:
                k.append(str(res)+"->"+str(nums[i]))
            else:
                k.append(str(nums[i]))
            i += 1
        return k
                
    