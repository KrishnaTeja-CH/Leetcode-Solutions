class Solution:
    def fib(self, n: int) -> int:
        #Recursion      return n if n<2 else self.fib(n-1) + self.fib(n-2)
        #Memoization
        if n < 2: return n 
        before , after = 0, 1
        for i in range(n):
            before, after = after, after+before
        return before
        
            
        
            
        