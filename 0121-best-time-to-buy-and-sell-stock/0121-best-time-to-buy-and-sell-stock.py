class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = sys.maxsize, 0
        for i in prices:
            buy = min(i, buy)
            sell = max(i-buy, sell)
        return sell
            
        
        