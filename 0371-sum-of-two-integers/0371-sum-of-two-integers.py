class Solution:
    def getSum(self, a: int, b: int) -> int:
        return int(log(exp(a)*exp(b))) if a != 0 and b != 0 else a or b         
