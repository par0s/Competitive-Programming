# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0
        
    def hasPathSum(self,root: TreeNode, sumGiven: int,sums = 0) -> bool:
        if root:
            arr = root 
            sums += root.val
            if root.left != None and root.right != None:
                return self.hasPathSum(root.left,sumGiven,sums) or self.hasPathSum(root.right,sumGiven,sums)
            elif root.left != None:
                return self.hasPathSum(root.left,sumGiven,sums)
            elif root.right != None:
                return self.hasPathSum(root.right,sumGiven,sums)
            else:
                if sums == sumGiven:
                    return True
        return False   
        
