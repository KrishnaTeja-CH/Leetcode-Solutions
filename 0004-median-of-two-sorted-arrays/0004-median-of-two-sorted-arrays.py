class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        x = len(nums)
        i = x//2
        if x%2 == 0:
            return (nums[i] + nums[i-1])/2
        else:
            return nums[i]
            