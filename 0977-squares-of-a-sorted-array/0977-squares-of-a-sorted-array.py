class Solution:
    def sortedSquares(self, N: List[int]) -> List[int]:
        l, r = 0, len(N) - 1
        ans = [0] * len(N)
        while l <= r:
            if abs(N[l]) > abs(N[r]):
                ans[r-l] = N[l] ** 2
                l += 1
            else:
                ans[r-l] = N[r] ** 2
                r -= 1   
        return ans
                    

        