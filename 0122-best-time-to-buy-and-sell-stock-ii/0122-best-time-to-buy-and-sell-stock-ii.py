class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        sol = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                sol += prices[i+1] - prices[i]
        return sol
             
# One-Liner
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))
            

 
            
        