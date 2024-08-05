class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, l, r = 0, 0, len(height)-1
        while l < r:
            area = (r-l) * min(height[l], height[r])
            res = max(res, area)
            l, r = (l + 1, r) if height[l] < height[r] else (l, r - 1)
        return res