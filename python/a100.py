# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def f(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            if p.val != q.val:
                return False
            return f(p.left, q.left) and f(p.right, q.right)
        
        return f(p, q)
