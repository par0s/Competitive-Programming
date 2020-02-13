class Solution:
    def __init__(self):
        self.dp = []
    def longestPalindromeSubseq(self, s: str) -> int:
        self.dp = [[0]  * len(s) for i in s]
        
        counter = 0
        start = 0
        end = 0
        
        while(counter < len(s)):
            self.dp[counter][counter] = 1
            counter += 1                    
                
        for j in range(len(s)):            
            for k in range(len(s)):
                if j == 0:
                    continue
                if k + j >= len(s):
                    break  
                start = k 
                end = k + j                                                      
                if s[start] == s[end]:
                    if end - start == 1:
                        self.dp[start][end] = 2
                    else:                                                 
                        self.dp[start][end] = 2 + self.dp[start + 1][end - 1]                        
                else:
                    if end - start == 1:
                        self.dp[start][end] = max(self.dp[start][start],self.dp[end][end])
                    else:
                        self.dp[start][end] = max(self.dp[start + 1][end],self.dp[start][end - 1])
                
        return self.dp[start][end]
