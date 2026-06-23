"""
 OOD: Yes
 Constraints: No
 input : constructor and method
 output : constructor and method
"""
# A.Clarify the goal : Design a Least Recently Used (LRU) cache that supports get and put operations in O(1) time complexity.
# B.Design the data structure : 
    # 1. HashMap : O(1) with LookUp to locate cache
    # 2. Doubly Linked List : O(1) to insert/delete/reorder nodes to record MRU, LRU
# C.Implement constructor and method

# Keywords: O(1) with insert/Delete/LookUp  -> HashMap
# Keywords: O(1) to insert/delete/reorder nodes -> Double linkedlist
# Image:  Imagine an instant-lookup Map Traverse an array to check if a Key or Value exists before , then perform following actions
# Image:  Hand-crafted double linkedlist with dummy head and tail to  record MRU, LRU
# Tricks:
    # 1. Dummy Boundary: Use dummy 'head' and 'tail' nodes to eliminate null pointer checks when adding/removing.
    # 2. Eviction: When cache exceeds capacity, evict 'tail.prev' because it represents the least recently used item.
    # 3. cache : {key: ListNode}

class ListNode:
    def __init__(self, key=0,val=0,next=None,prev=None):
        self.key = key
        self.val = val
        self.next = next  # 修正：原本誤寫為 self.head
        self.prev = prev
class LRUCache:
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.cache = {} #{key : ListNode}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key:int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node) # remove from the end : LRU
            self._insert(node) # insert at the head, MRU
            return node.val
        return -1
    
    def put(self, key:int, val:int):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self._remove(node) # remove from the end : LRU
            self._insert(node) # insert at the head, MRU
        else:
            node = ListNode(key,val)
            self.cache[key] = node
            self._insert(node) # insert at the head, MRU
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node) # remove from the end : LRU
                del self.cache[lru_node.key]
                
    def _remove(self, node:ListNode):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node:ListNode):
        nxt = self.head.next
        self.head.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = self.head


# Time Complexity:  
#   - LRUCache(capacity): O(1) -> Initializing pointers and variables takes constant time.
#   - get(key):           O(1) -> Average time for hash map lookup and pointer updates is constant.
#   - put(key, value):    O(1) -> Inserting into hash map and moving nodes both take constant time.
# Space Complexity: O(capacity) -> The hash map and doubly linked list store at most 'capacity' nodes.
         