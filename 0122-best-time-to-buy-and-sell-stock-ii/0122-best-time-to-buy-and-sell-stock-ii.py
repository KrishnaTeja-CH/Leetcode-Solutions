class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        ''''mini, maxi, sol = sys.maxsize, 0, 0
        for i in prices:
            mini = min(i, mini)
            profit = i - mini
            if profit > maxi:
                mini = i
                sol += profit
            else:
                maxi = max(profit, maxi)
        return sol'''


#Type - 2 
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1] - prices[i]
        return profit
 
            
        