class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = Counter(nums)
        for i in s:
            if s[i]==1 :
                return i
        