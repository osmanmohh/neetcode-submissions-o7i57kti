# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def makeArr(self, list1):
        if not list1:
            return None
        curr = list1
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res[::-1]

    def makeLinkedList(self, arr):
        if not arr:
            return None
        
        res = ListNode(-1)
        curr = ListNode(arr[0])
        res.next = curr
        for num in arr[1:]:
            curr.next = ListNode(num)
            curr = curr.next
        return res.next



    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return(self.makeLinkedList(self.makeArr(head)))


