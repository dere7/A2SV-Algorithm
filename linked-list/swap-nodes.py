# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow=fast=left=head
        for _ in range(k - 1):
            left = left.next
            fast = fast.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        left.val, slow.val = slow.val, left.val
        return head