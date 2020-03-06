# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.preOrder(s, t)

    def preOrder(self, s, t):
        same = self.contain(s, t)
        if same:
            return True
        if s == None:
            return False

        return self.preOrder(s.left, t) or self.preOrder(s.right, t)
    
    def contain(self, s, t):
        if t == None and s == None:
            return True
        
        if s == None or t == None:
            return False
        
        if s.val != t.val:
            return False
        
        return self.contain(s.left, t.left) and self.contain(s.right, t.right)

#法2
class Solution:
    # 前序遍历
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        ss = self.pre_order(s)
        tt = self.pre_order(t)
        if tt in ss:
            return True
        else:
            return False
    def pre_order(self,root):
        if not root:
            return '#'  # 用井号作为单孩子的结尾，双井号为叶子节点结尾
        # 用星号作为各节点值的开头
        return '*' + str(root.val)  + self.pre_order(root.left) + self.pre_order(root.right)
