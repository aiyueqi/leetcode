# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return
        l = head
        r = head.next
        while r != None:
            if l.val == r.val:
                l.next = r.next
                r = l.next
            else:
                l = r
                r = r.next
        return head

#法2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return
        l = head
        r = head.next
        while r != None:
            if l.val == r.val:
                r = r.next
            else:
                l.next = r
                l = r
                r = l.next
        l.next = None
        return head
