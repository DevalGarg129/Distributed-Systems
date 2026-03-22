class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0) #MRU
        self.tail = Node(0, 0) #LRU
        self.head.next = self.tail
        self.tail.prev = self.head


    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def _insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node


    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.value
    
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

cache = LRUCache(2)
cache.put("SELECT * FROM users", "Result1")
cache.put("SELECT * FROM orders", "Result2")
print(cache.get("SELECT * FROM users"))
cache.put("SELECT * FROM products", "Result3")



