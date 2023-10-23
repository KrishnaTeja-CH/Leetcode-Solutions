class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
#Two Pointer
        l, r = 0, len(numbers)-1
        while l < r:
            sol = numbers[l] + numbers[r]
            if sol == target:
                return [l+1, r+1]
            elif sol > target:
                r -= 1
            else:
                l += 1
#Hashmap
        '''
        sol = {}
        for i in range(len(numbers)):
            k = target - numbers[i]
            if k in sol:
                return [sol[k]+1, i+1]
            sol[numbers[i]] = i
        '''            
         