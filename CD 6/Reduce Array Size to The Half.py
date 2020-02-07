class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dicts = {}
        toSort = []        
        halfSize = len(arr)//2
        
        for i in arr:
            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1
        
        for i in dicts:
            toSort.append(tuple([i,dicts[i]]))
        
        toSort.sort(key = lambda x: x[1])
        
        lenCounter = 0
        returnCounter = 0
        
        #print(toSort)
        
        for i in toSort[::-1]:
            lenCounter += i[1]
            returnCounter += 1
            
            if lenCounter >= halfSize:
                return returnCounter
            
        
        
        
