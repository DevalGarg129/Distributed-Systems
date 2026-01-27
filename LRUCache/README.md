# Functional Requirements:
Browser Tab Cache must:
Store recently opened tabs
Retrieve tab instantly when revisited
Update tab recency when visited again
Evict tab when memory capacity is full
Evict the Least Recently Used (LRU) tab
Maintain fixed capacity (configurable)
Support operations:
    open_tab(key, page)
    visit_tab(key)
    evict_if_needed()

# Non functional Requirements
Low Latency 
DEterministic eviction policy
Efficient memory use
scalable with usage burst
consistency

# Ques 1: Why LRU is used not FIFO??
Ans : FIFO eviction fails because it evicts oldest arrival even if recently used.

Browser behavior aligns with temporal locality:
“Tabs recently used → likely re-used again”

Example FIFO failure:
User:
A → B → C → revisit A → open D

FIFO evicts A even though it was just used
LRU evicts B (correct behavior)

# Complexity Analysis : open/get, visit, evict, store = O(1), space = O(capacity)

# Algorithm : 
On open_tab(key):
    Insert node at head (MRU)
    If full → remove tail (LRU)

On visit_tab(key):
    Lookup in hashmap
    Move node to head (MRU)

On eviction:
    Remove tail node
    Delete entry from hashmap

# Data Structure used : 
    for CacheLookUp = HashMap
    Recency Order = Doubly Linked List
    Combine = HashMap + DLL