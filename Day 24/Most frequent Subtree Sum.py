# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.array = []
        
    def possibleSum(self,root):
        if root == None:
            return 
        else:                        
            self.array.append(self.sumBelow(root))            
            self.possibleSum(root.left)
            self.possibleSum(root.right)
        
    def findFrequentTreeSum(self,root: TreeNode) -> List[int]:
        self.possibleSum(root)        
        dicts = {}        
        maxs = 0
        answer = []
        
        for i in self.array:
            if i != None:
                if i in dicts:
                    dicts[i] += 1                
                else:
                    dicts[i] = 0

                if dicts[i] > maxs:
                    maxs = dicts[i]
                
        for i in dicts:
            if dicts[i] == maxs:
                answer.append(i)
            
        print(self.array)
        return answer
    
    def sumBelow(self,root):
        if root == None:
            return 
        total = root.val
        leftTotal = self.sumBelow(root.left)
        rightTotal = self.sumBelow(root.right)        
                
        if leftTotal != None:
            total += leftTotal
        if rightTotal != None:
            total += rightTotal
        
        #print(root.val,total,self.array)
        return total
        
        
