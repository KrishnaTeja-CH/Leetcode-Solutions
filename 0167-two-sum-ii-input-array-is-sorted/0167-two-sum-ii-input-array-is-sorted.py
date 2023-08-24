class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
# Hashmap
        '''sol ={}
        for i in range(len(numbers)):
            k = target - numbers[i]
            if k in sol:
                return [sol[k]+1, i+1]
            sol[numbers[i]] = i'''

# Two Pointer
        s, t  = 0, len(numbers)-1
        while s < t:
            sol = numbers[s] + numbers[t]
            if sol == target: return [s+1, t+1]
            elif sol < target: s += 1
            else: t -= 1
                
                
