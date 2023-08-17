class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sol = []
        for i in range(len(accounts)):
            sol.append(sum(accounts[i]))
        return max(sol)
        