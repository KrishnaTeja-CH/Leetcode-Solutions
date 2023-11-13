class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff, res = 0, 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(cost)):
            diff += gas[i] - cost[i]
            if diff < 0:
                diff = 0
                res = i+1
        return res
            