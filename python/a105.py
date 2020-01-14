from typing import List, Dict, Tuple
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.f(0, len(preorder)-1, 0, len(preorder)-1, preorder, inorder)

    def f(self, pl, pr, il, ir, A, B):
        if pl>pr:
            return None

        root = TreeNode(A[pl])
        index = -1
        for t in range(il, ir+1):
            if A[pl] == B[t]:
                index = t
                break

        ltreelen = index - il
        root.left = self.f(pl+1, pl+ltreelen, il, index-1, A, B)
        root.right = self.f(pl+ltreelen+1, pr, index+1, ir, A, B)

        return root

s = Solution()
result = s.buildTree([1,2,3], [3,2,1])
print(result.left.left.val)
