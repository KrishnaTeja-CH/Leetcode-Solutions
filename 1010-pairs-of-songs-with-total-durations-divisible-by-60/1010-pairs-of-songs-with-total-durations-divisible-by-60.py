class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        count = [0] * 60
        for i in time:
            res += count[-i%60]
            count[i%60] += 1
        return res
		
		
        