# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        t = head
        while l1!= None and l2!= None:
            if l1.val < l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            t = t.next
        
        if l1 != None:
            t.next = l1
        else:
            t.next = l2

        return head.next

        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.f(l1, l2)

#递归
    def f(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.f(l1.next, l2)
            return l1
        else:
            l2.next = self.f(l1, l2.next)
            return l2
