class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for i, j in enumerate(nums):
            if j in hm and abs(i-hm[j]) <=k:
                return True
            hm[j] = i


        