class Solution:
    def __init__(self):
        self.arr = [] 
        for i in range(101):
            lst = []
            for j in range(101):
                lst.append(0)
            self.arr.append(lst)                
        self.arr[0][0] = 1
        
    def uniquePaths(self, m: int, n: int) -> int:
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    self.arr[i][j] = self.arr[i][j - 1]                    
                if j == 0:
                    self.arr[i][j] = self.arr[i - 1][j]
                else:
                    self.arr[i][j] = self.arr[i][j - 1] + self.arr[i - 1][j]
                #print(self.arr)
        return self.arr[i][j]
        
        
