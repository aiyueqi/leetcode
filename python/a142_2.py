# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        fast,slow=head,head
        while True:
            if fast and fast.next:
                fast=fast.next.next
            else:
                return None
            slow=slow.next
            if fast==slow:
                break

        fast=head
        while fast!=slow:
            fast,slow=fast.next,slow.next
        return fast
