from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            temp = head
            length = 0
            while temp:
                length += 1
                temp = temp.next
            mid = length // 2
            for _ in range(mid):
                head = head.next
            return head