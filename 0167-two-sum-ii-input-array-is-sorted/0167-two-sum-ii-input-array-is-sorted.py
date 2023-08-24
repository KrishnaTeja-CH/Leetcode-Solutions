class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
# Hashmap
        sol ={}
        for i in range(len(numbers)):
            k = target - numbers[i]
            if k in sol:
                return [sol[k]+1, i+1]
            sol[numbers[i]] = i
        
            


                
                
