class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right  = [0] * n, [0] * n
        res = 0

        for i in range(1, n):
            left[i] = max(left[i-1], height[i-1])
        print("left = " ,left)

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        print("right =" , right)

        for i in range(n):
            res += max(0, min(right[i], left[i]) - height[i])
        return res
        