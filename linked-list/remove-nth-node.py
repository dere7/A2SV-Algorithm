from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=slow=head
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        if not fast:
            head = head.next
        elif slow.next:
            # slow.val = slow.next.val
            slow.next = slow.next.next
        else:
            head = None
        return head 