from typing import List, Dict, Tuple

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

#     def f(self, p, q):
#         if p == q: return p
#         tmp = p.next
#         p.next = q.next
#         q.next = p
#         return self.f(tmp, q)
    
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head == None:
#             return None
#         tail=head
#         while tail.next != None:
#             tail = tail.next
#         return self.f(head, tail)

#迭代法
	# def reverseList(self, head: ListNode) -> ListNode:
 #        p = None
 #        q = head
 #        while(q):
 #            tmp = q.next
 #            q.next = p
 #            p = q
 #            q = tmp
 #        return p

#递归解法
    def f(self, p, q):
        if q == None: return p
        tmp = q.next
        q.next = p
        return self.f(q, tmp)
    
    def reverseList(self, head: ListNode) -> ListNode:
        return self.f(None, head)
    