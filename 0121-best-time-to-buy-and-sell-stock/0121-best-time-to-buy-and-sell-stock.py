class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini, maxi = sys.maxsize, 0
        for i in prices:
            mini = min(i, mini)
            profit = i - mini
            maxi = max(profit, maxi)
        return maxi
            
        
        
