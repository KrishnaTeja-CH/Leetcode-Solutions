class Solution:
    def countPrimes(self, n: int) -> int:
        if n <2: return 0
        primes = [1]*n
        primes[0] = primes[1] = 0
        i = 2
        while(i*i < n):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = 0
            i+= 1
        return sum(primes)

        
            
    

        
        