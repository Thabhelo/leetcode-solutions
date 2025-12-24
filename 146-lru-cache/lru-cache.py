class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps key -> Node

        # Initialize dummy nodes
        self.left = Node(0, 0)  # LRU (Least Recently Used)
        self.right = Node(0, 0) # MRU (Most Recently Used)

        # Connect dummy nodes: [Left] <-> [Right]
        self.left.next = self.right
        self.right.prev = self.left

    # Helper: Remove node from linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Helper: Insert node at right (Most Recent)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # We accessed it, so make it Most Recently Used
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If exists, remove old version so we can re-insert as new
            self.remove(self.cache[key])
        
        # Create a new node and insert it at the MRU position
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If over capacity, remove the LRU node (the one after Left dummy)
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]