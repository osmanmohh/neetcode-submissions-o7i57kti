# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 
        # find middle node
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        l1, l2 = head, slow.next
        slow.next = None

        # revesse
        prev = None
        curr = l2
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l2 = prev


        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            l1.next = l2
            l2.next = temp1
            
            l1 = temp1
            l2 = temp2

