from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        meet = self.hasCycle(head)
        if not meet:
            return None

        return self.findIndex(head, meet)

    def hasCycle(self, head):
        slow = head
        fast = head
        while fast != None:
            slow = slow.next
            fast = fast.next
            if fast == None:
                return None

            fast = fast.next
            if slow == fast:
                return slow 
        return False

    def countCycle(self, meet):
        slow = meet.next
        fast = meet.next.next

        count = 1 
        while slow != fast:
            slow = slow.next
            fast = fast.next.next
            count += 1

        return count

    def findIndex(self, head, meet):
        cycleSize = self.countCycle(meet)

        fast = head
        slow = head

        for i in range(0, cycleSize):
            fast = fast.next

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
