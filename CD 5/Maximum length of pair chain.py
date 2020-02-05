class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs)
        dp = [1]
        maxer = 1
        for i in range(len(pairs)):
            if i == 0:
                continue
            index = i - 1
            while(index >= 0 and pairs[i][0] <= pairs[index][1]):
                index -= 1
            if index < 0:                
                dp.append(1)
            else:                
                dp.append(dp[index] + 1)
            if dp[-1] > maxer:
                maxer = dp[-1]
            #print(dp,i,index,pairs[i][0],pairs[index][1],index,pairs[i][0] <= pairs[index][1])
        return maxer
            
