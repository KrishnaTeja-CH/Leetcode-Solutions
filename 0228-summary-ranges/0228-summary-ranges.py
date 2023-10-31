class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i,j,k = 0, len(nums), []
        while i < j:
            res = nums[i]
            while i+1 < j and nums[i]+1 == nums[i+1]:
                i += 1
            if res != nums[i]:
                k.append(str(res)+"->"+str(nums[i]))
            else:
                k.append(str(nums[i]))
            i += 1
        return k
            
    