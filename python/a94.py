# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#迭代
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        p = root
        while True:
            if p != None:
                stack.append(p)
                p = p.left
                continue
            if len(stack) == 0:
                break
            tmp = stack.pop()
            result.append(tmp.val)
            p = tmp.right
        return result
#递归
        # result = []

        # def f(node):
        #     if node == None:
        #         return
        #     f(node.left)
        #     result.append(node.val)
        #     f(node.right)

        # f(root)
        # return result
        
