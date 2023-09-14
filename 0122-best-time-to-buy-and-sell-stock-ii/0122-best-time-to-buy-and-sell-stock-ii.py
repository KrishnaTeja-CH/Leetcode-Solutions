class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        mini, maxi, sol = sys.maxsize, 0, 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                sol += prices[i+1] - prices[i]
        return sol
                
            

 
            
        