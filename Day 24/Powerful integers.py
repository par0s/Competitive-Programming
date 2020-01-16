class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        powerfuls = set()
        
        pairs = []
        
        if y == 1:
            yUpper = 1
        else:
            yUpper = math.log(bound,y)
        
        
        if x == 1:
            xUpper = 1
        else:
            xUpper = math.log(bound,x)
        
        
        
            
        
        for i in range(int(xUpper + 1)):
            for j in range(int(yUpper + 1)):
                sumProduct = x ** i + y ** j
                pairs.append([i,j,sumProduct])
                if sumProduct <= bound:
                    powerfuls.add(sumProduct)
                
        return powerfuls
