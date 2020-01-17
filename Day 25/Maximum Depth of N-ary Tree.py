# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):       
        self.max = 0
    def maxDepth(self, root: 'Node',height = 1) -> int:
        if self.max < height:
            self.max = height
            
        for i in root.children:
            self.maxDepth(i,height + 1)
        
        return self.max
        
            
            
