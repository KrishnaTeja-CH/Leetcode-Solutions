class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        print(stones)
        sol = 0
        for i in stones:
            if i in jewels:
                sol += 1
        return sol
        