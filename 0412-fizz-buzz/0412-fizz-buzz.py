class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sol = []
        for i in range(1, n+1):
            if i%15 == 0:
                i = "FizzBuzz"
            elif i%3 == 0: 
                i = "Fizz"
            elif i%5 ==0:
                i = "Buzz"
            sol.append(str(i))
        return sol
            
        