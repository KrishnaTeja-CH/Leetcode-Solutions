class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = sys.maxsize
        res = []
        maxi = 0
        for i in prices:
            mini = min(i, mini)
            profit = i - mini
            if profit > maxi:
                mini = i
                res.append(profit)
            else:
                maxi = max(profit, maxi)
        return sum(res)
                
            
        