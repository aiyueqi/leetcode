from typing import List, Dict, Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0
    result = 0
    def mid(self, p, k):
        if p == None:
            return
        else:
            self.mid(p.left, k)
            self.count += 1
            if self.count == k:
                self.result = p.val
                return
            self.mid(p.right, k)
        
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.mid(root, k)
        return self.result