class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    #print(grid[i][j],grid[i][j - 1],end = " ")
                    grid[i][j] += grid[i][j - 1]                  
                elif j == 0:
                    grid[i][j] += grid[i - 1][j] 
                else:
                    grid[i][j] += min(grid[i][j - 1],grid[i - 1][j]) 
                #print(grid,(i,j),grid[i][j])
        return grid[i][j]
