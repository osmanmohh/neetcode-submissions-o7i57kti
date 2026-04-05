class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def moveToFront(self, key: int) -> None:
        node = self.cache[key]

        node.prev.next = node.next
        node.next.prev = node.prev
         

        node.next = self.head.next
        self.head.next.prev = node

        node.prev = self.head
        self.head.next = node


    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        self.moveToFront(key)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.moveToFront(key)
            self.cache[key].val = value
            return
        
        if len(self.cache) >= self.capacity:
            lru = self.tail.prev
            lru.prev.next = self.tail
            self.tail.prev = lru.prev
            del self.cache[lru.key]

        newNode = Node(key, value)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        self.cache[key] = newNode





