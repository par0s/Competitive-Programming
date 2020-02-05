import math
class Solution:
    def climbStairs(self, n: int) -> int:
        #print(self.fib(n - 1) ,self.fib(n - 2))
        return self.fib(n - 1) + self.fib(n - 2)
    
    

    def fib(self,n: int):
        n = n + 1        
        PHI = (1 + math.sqrt(5)) / 2
        return int(PHI ** n / math.sqrt(5) + 0.5)
        
