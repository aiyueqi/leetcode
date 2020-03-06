# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.f(root, root)

    def f(self, a, b):
        if not a and not b:
            return True
        
        if not a or not b:
            return False

        if a.val != b.val:
            return False
        
        return self.f(a.left, b.right) and self.f(a.right, b.left)
