# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        return self.f(root, 0, sum)

    def f(self, root, pathsum, sum):
        if root == None:
            return False

        pathsum += root.val

        if root.left == None and root.right == None:
            return pathsum == sum
            
        return self.f(root.left, pathsum, sum) or \
        self.f(root.right, pathsum, sum)
