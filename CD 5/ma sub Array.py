class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        previous = -99999999999999999999
        max = -99999999999999999999
        for i in nums:
            if i > previous + i:
                previous = i
            else:
                previous += i            
            if previous > max:
                max = previous
        
        return max
            
