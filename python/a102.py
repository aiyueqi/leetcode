# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        queue = []
        level_queue = []
        result = []
        if root == None:
            return []
        
        def add(p, level):
            if p == None:
                return
            queue.append(p)
            level_queue.append(level)

        queue.append(root)
        level_queue.append(0)
        while queue:
            p = queue.pop(0)
            level = level_queue.pop(0)
            add(p.left, level+1)
            add(p.right, level+1)
        
            if len(result) <= level:
                result.append([])
                
            result[level].append(p.val)

        return result

#别人的解法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        queue = []
        queue.append(root)
        while queue:
            tmp = []
            n_queue = []
            for node in queue:
                if node:
                    tmp.append(node.val)
                    n_queue.append(node.left)
                    n_queue.append(node.right)
            queue = n_queue
            if tmp:
                res.append(tmp)
        return res
