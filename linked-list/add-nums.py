from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = temp3 = None
        temp1 = l1
        temp2 = l2
        carry = 0
        while temp1 or temp2:
            val1 = temp1.val if temp1 else 0
            val2 = temp2.val if temp2 else 0
            sum_num = val1 + val2 + carry
            carry = sum_num // 10
            node = ListNode(sum_num % 10)
            if temp3:
                temp3.next =  node
                temp3 = temp3.next
            else:
                result = node
                temp3 = result
            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None
        if carry != 0:
            node.next = ListNode(carry)
        return result
