class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0   
        
        if len(nums) < 2:
            return nums[0]
        
        self.dp = [nums[0],nums[1]]
        
        for i in range(len(nums)):
            if i < 2:
                continue
            if i == 2:
                self.dp.append(nums[i] + nums[0])
            else:
                #if i == 4:
                    #print(self.dp[i - 2] + nums[i],self.dp[i - 3] + nums[i])
                self.dp.append(max(nums[i] + self.dp[i - 2],nums[i] + self.dp[i - 3]))
        
        #print(self.dp)
        return max(self.dp[-2],self.dp[-1])
            
