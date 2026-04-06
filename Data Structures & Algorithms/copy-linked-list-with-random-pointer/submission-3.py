"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        oldToNew = {}
        curr = head
        while curr:
            newNode = Node(curr.val, None, None)
            oldToNew[curr] = newNode
            curr = curr.next
        curr = head
        while curr:
            oldToNew[curr].next = oldToNew[curr.next] if curr.next else None
            oldToNew[curr].random = oldToNew[curr.random] if curr.random else None
            curr = curr.next
        return oldToNew[head]



         
