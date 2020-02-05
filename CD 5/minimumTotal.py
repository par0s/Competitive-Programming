class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        
        elif len(triangle) == 1:
            return min(triangle[0])
        
        triangle = triangle[::-1]
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i - 1][j],triangle[i - 1][j + 1])
            
        return triangle[i][j]
            
