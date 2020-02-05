class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        if len(self.nums) > 0:
            self.dp = [self.nums[0]]
        
        for i in range(len(nums)):
            if i == 0:
                continue
            self.dp.append(self.dp[i - 1] + self.nums[i])
    
    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j] - self.dp[i] + self.nums[i]
