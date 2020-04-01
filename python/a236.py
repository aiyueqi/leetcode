# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root, p, q)
        return self.result

    def dfs(self, node, p, q):
        if node == None:
            return 0
        l = self.dfs(node.left, p, q)
        r = self.dfs(node.right, p, q)
        mine = 0
        if node == p or node == q:
            mine = 1
        result = l+r+mine
        if self.result == None and result == 2:
            self.result = node
        return result

