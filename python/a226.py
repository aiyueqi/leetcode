# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.f(root)
        return root

    def f(self, root):
        if root == None:
            return
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.f(root.left)
        self.f(root.right)
