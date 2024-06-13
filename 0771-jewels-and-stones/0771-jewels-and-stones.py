class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(x in set(jewels) for x in stones)
        