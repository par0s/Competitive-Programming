class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        toSort = []
        sortedIndex = []
        
        for i in range(len(mat)):
            numOfSoldiers = self.soldierCount(mat[i])
            posNum = tuple([numOfSoldiers,i])
            toSort.append(posNum)
        
        toSort = sorted(toSort)
        
        for j in toSort:
            sortedIndex.append(j[1])
        
        return sortedIndex[:k]
    
    
    def soldierCount(self,row):
        return row.count(1)
        
