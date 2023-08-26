class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini, maxi, res = sys.maxsize, 0, []
        for i in prices:
            mini = min(i, mini)
            profit = i - mini
            if profit > maxi:
                mini = i
                res.append(profit)
            else:
                maxi = max(profit, maxi)
        return sum(res)
            
        