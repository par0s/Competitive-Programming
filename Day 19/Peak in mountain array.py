class Solution:
    def peakIndexInMountainArray(self, lst: List[int]) -> int:
        for i in range(1,len(lst)):
            if lst[i - 1] < lst[i] and lst[i] > lst[i + 1]:
                return i
            
            
        
