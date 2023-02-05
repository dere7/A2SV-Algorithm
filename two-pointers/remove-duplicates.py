from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        head = prev = ListNode()
        head.next = curr
        while curr and curr.next:
            if curr.val == curr.next.val:
                while(curr and curr.next and 
                      curr.val == curr.next.val):
                    curr = curr.next
                curr = curr.next
                prev.next = curr
            else:
                prev = prev.next
                curr = curr.next
        return head.next
