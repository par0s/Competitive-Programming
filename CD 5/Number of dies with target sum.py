class Solution:
    def __init__(self):
        self.dp = {}
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        val = tuple([d,target])
        
        if val in self.dp:
            return self.dp[val]
        
        if d < 0 or target < 0:            
            self.dp[val] = 0
            return 0
        
        if target == 0 and d == 0:            
            self.dp[val] = 1
            return 1
        
        if target == 0 and d > 0:
            self.dp[val] = 0
            return 0
        
        ways = 0
        for i in range(1,f+1):
            ways += self.numRollsToTarget(d - 1,f,target - i)
        
        self.dp[val] = ways
                
        return ways % (10 ** 9 + 7)
            
        
