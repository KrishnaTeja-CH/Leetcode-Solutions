class Solution:
    def minimumChairs(self, s: str) -> int:
        sol = res = 0
        for i in s:
            sol += 1 if i == 'E' else -1
            res = max(sol, res)
        return res