# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        extra = 0
        result = ListNode(-1)
        point = result
        while p!=None or q!=None or extra!=0:
            tmp = extra
            tmp += p.val if p else 0
            tmp += q.val if q else 0
            now = tmp%10
            extra = tmp//10
            point.next = ListNode(now)
            
            point = point.next
            p = p.next if p else p
            q = q.next if q else q
            
        return result.next
