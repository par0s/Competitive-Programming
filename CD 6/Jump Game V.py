class Solution:
    def __init__(self):
        self.dict = {}        
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        self.max = 0
        
        for i in range(len(arr)):            
            self.max = max(self.max,self.subJumps(arr,i,d))  
        return self.max
            
            
    
    def subJumps(self,arr,i,d):            
        if i in self.dict:
            return self.dict[i]
        
        canGo = self.canJump(arr,i,d)        
        if len(canGo) == 0:
            self.dict[i] = 1
            return 1
        else:
            total = 0
            for j in canGo:
                total = max(total,self.subJumps(arr,j,d))
        
        self.dict[i] = total + 1
        
        return total + 1
        
    
    
    def canJump(self,arr,i,d):
        back = i - d
        if back < 0:
            back = 0
        
        front = i + d
        
        if front >= len(arr):
            front = len(arr) - 1
        
        canGo = []
            
        backGo = i - 1
        
        while(backGo >= back):        
            if backGo == i:
                continue
            if arr[backGo] >= arr[i]:
                break
            else:
                canGo.append(backGo)
            backGo -= 1            
        
        frontGo = i + 1
        
        while(frontGo <= front):            
            if frontGo == i:
                continue
            if arr[frontGo] >= arr[i]:
                break
            else:
                canGo.append(frontGo)            
            frontGo += 1                        
        return canGo
            
            
            
