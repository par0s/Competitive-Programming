# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.possibleSums = []
        
    def maxProduct(self, root: TreeNode) -> int:
        if not root:
            return 0
        rootTotal = self.notFun(root)
        self.maxSplit = 0
        
        def inOrder(root):
            if root:                
                inOrder(root.left)
                self.maxSplit = max((rootTotal - root.val) * root.val,self.maxSplit)
                inOrder(root.right)
            else:
                return 0                        
        
        inOrder(root)
        return self.maxSplit % ((10 ** 9) + 7)
    
    def notFun(self,root):        
        if not root:
            return 0
        else:
            root.val = root.val + self.notFun(root.left) + self.notFun(root.right)
            #self.possibleSums.append(total)
            return root.val
            
            
