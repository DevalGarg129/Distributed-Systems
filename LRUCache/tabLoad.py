class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class TabLRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # dummy head (MRU) and tail (LRU)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def switchTab(self, key):
        # get operation
        if key not in self.cache:
            return None

        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.value

    def openTab(self, key, value):
        # put operation
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            del self.cache[key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_to_head(new_node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

cache = TabLRUCache(3)
cache.openTab(1, "youtube.com")
cache.openTab(2, "gmail.com")
cache.openTab(3, "reddit.com")
print(cache.switchTab(1))