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
        map = {}
        if head is None: return None
        cur = head
        while cur:
            map[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = map[cur]
            copy.random = map[cur.random] if cur.random else None
            copy.next = map[cur.next] if cur.next else None
            cur = cur.next
        return map[head]

        

        
        