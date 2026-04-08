# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        carry = 0
        while l1 or l2 or carry: # 8 + 5 = 13 -> val = 3, carry = 1
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry # 13
            carry = val // 10 # 1
            val = val % 10 # 3

            curr.next = ListNode(val)
            curr = curr.next

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next
        return dummy.next

