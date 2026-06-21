"""
 OOD: Yes
 Constraints: No
 input : constructor and method
 output : constructor and method
"""
# A.Clarify the goal : Design a Least Recently Used (LRU) cache that supports get and put operations in O(1) time complexity.
# B.Design the data structure : 
    # 1. HashMap : O(1) with LookUp to locate cache
    # 2. Doubly Linked List : O(1) to insert/delete/reorder nodes
# C.Implement constructor and method

# Keywords: O(1) with insert/Delete/LookUp  -> HashMap
# Keywords: O(1) to insert/delete/reorder nodes -> Double linkedlist
# Image:  Imagine an instant-lookup Map Traverse an array to check if a Key or Value exists before , then perform following actions
# Image:  Hand-crafted double linkedlist with dummy head and tail
# Tricks:
    # 1. Dummy Boundary: Use dummy 'head' and 'tail' nodes to eliminate null pointer checks when adding/removing.
    # 2. Eviction: When cache exceeds capacity, evict 'tail.prev' because it represents the least recently used item.

class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:
    def __init__(self,capacity:int):
        self.capacity = capacity
        self.cache = {} #Key: ListNode
        # 初始化虚拟头尾节点，防止链表断裂与处理空指针边界
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail 
        self.tail.prev = self.head
    
    def get(self, key:int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Update doubly Linked List  - 用来记录 LRU, MRU
            self._remove(node) # delete from the current position
            self._insert(node) # insert at the head, MRU
            return node.val
        return -1

    def put(self, key:int, newValue:int)->None:
        if key in self.cache:
            node = self.cache[key]
            node.val = newValue
            # Update doubly Linked List  - 用来记录 LRU, MRU
            self._remove(node)  # delete from the current position
            self._insert(node) # insert at the head, MRU
        else:
            new_node = ListNode(key,newValue)
            self.cache[key] = new_node
            # Update doubly Linked List  - 用来记录 LRU, MRU
            self._insert(new_node) # insert at the head, MRU
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)  # delete from the current position
                del self.cache[lru_node.key] # 从哈希表中释放内存    
    def _remove(self,node:ListNode)-> None:
        """内部辅助函数：将节点从双向链表中抽离 (断开前后连接)"""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    def _insert(self,node:ListNode)-> Node:
        """内部辅助函数：将节点插入到虚拟头节点后方 (代表最新使用 MRU)"""
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node
    

# Time Complexity:  
#   - LRUCache(capacity): O(1) -> Initializing pointers and variables takes constant time.
#   - get(key):           O(1) -> Average time for hash map lookup and pointer updates is constant.
#   - put(key, value):    O(1) -> Inserting into hash map and moving nodes both take constant time.
# Space Complexity: O(capacity) -> The hash map and doubly linked list store at most 'capacity' nodes.
         