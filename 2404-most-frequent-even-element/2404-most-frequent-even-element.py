class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = 0
        num = -1
        nums.sort()
        for i in nums:
            if i%2 == 0:
                if nums.count(i) > count:
                    count = nums.count(i)
                    num = i
        return num