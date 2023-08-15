class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        t = len(numbers)-1
        while s < t:
            sol = numbers[s] + numbers[t]
            if sol == target:
                return [s+1, t+1]
            elif sol < target :
                s += 1
            else:
                t -= 1
                
                
