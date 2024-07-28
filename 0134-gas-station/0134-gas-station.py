class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = res = 0
        for i in range(len(cost)):
            total += gas[i] - cost[i]
            if total < 0:
                total, res = 0, i+1
        return res
