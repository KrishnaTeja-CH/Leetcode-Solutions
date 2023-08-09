class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        max_price = 0 

        for i in prices:
            min_price = min (min_price, i)
            profit  = i - min_price
            max_price = max(max_price, profit)
        return max_price