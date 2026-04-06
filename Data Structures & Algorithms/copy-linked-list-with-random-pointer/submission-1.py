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
        oldToNew = {}
        curr = head
        while curr:
            newNode = Node(curr.val, None, None)
            oldToNew[curr] = newNode
            curr = curr.next

        curr = head
        while curr:
            newNode = oldToNew[curr]
            newNode.next = oldToNew[curr.next] if curr.next else None
            newNode.random = oldToNew[curr.random] if curr.random else None
            curr = curr.next
        return oldToNew[head] if head else None

         
