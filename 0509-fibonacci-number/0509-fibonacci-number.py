class Solution:
    def fib(self, n: int) -> int:
        #Recursion      return n if n<2 else self.fib(n-1) + self.fib(n-2)
        #Memoization
        if n < 2: return n 
        prev1, prev2, output = 1, 0, 0
        for i in range(2, n+1):
            output = prev1 + prev2
            prev2 = prev1
            prev1 = output
        return output
        
        
            
        
            
        