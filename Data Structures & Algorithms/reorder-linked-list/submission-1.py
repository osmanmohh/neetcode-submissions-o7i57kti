# [0, 1, 2, 3]
# [6, 5, 4]
# [0, 6, 1, 5, 2, 4, 3]

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None

        # reverse l2
        prev = None
        curr = l2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        l2 = prev
        # merge 2 lists
        dummy = ListNode(-1)
        dummy.next = l1
        while l1 and l2:
            temp1 = l1.next
            l1.next = l2
            temp2 = l2.next
            l2.next = temp1
            l1 = temp1
            l2 = temp2
        head = dummy.next


