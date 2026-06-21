"""
 OOD: Yes
 Constraints: No
 input : constructor and method
 output : constructor and method
"""
# A.Clarify the goal : Design a Least Recently Used (LRU) cache that supports get and put operations in O(1) time complexity.
# B.Design the data structure : 
#     1. HashMap : O(1) with LookUp to locate nodes instantly -> dict (key -> ListNode)
#     2. Doubly Linked List : O(1) to insert/delete/reorder nodes -> Hand-crafted list with dummy head and tail
# C.Implement constructor and method

# Tricks:
#     1. Dummy Boundary: Use dummy 'head' and 'tail' nodes to eliminate null pointer checks when adding/removing.
#     2. Eviction: When cache exceeds capacity, evict 'tail.prev' because it represents the least recently used item.

class ListNode:
    """双向链表节点定义"""
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # HashMap: key -> ListNode
        
        # 初始化虚拟头尾节点，防止链表断裂与处理空指针边界
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        """内部辅助函数：将节点从双向链表中抽离 (断开前后连接)"""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_head(self, node: ListNode) -> None:
        """内部辅助函数：将节点插入到虚拟头节点后方 (代表最新使用 MRU)"""
        n = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        node.next = n
        n.prev = node

    def get(self, key: int) -> int:
        # Step 2: Implement get method
        if key in self.cache:
            node = self.cache[key]
            # Update doubly Linked List - 用来记录 LRU, MRU
            self._remove(node)       # 先从原位置拔出
            self._add_to_head(node)  # 重新插回最前面（代表最新鲜）
            # 回传 Cache 值
            return node.val
        # 回传 Cache 值（未命中返回 -1）
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Key 已存在：更新数值，并将其移至头部刷新活跃度
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Key 不存在：新建节点并存入哈希表与链表头部
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            
            # 如果缓存容量超限，剔除最久未使用的节点
            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev       # 虚拟尾节点的前驱就是最老节点（LRU）
                self._remove(lru_node)          # 从链表中删除
                del self.cache[lru_node.key]    # 从哈希表中释放内存

# Time Complexity:  
#   - LRUCache(capacity): O(1) -> Initializing pointers and variables takes constant time.
#   - get(key):           O(1) -> Average time for hash map lookup and pointer updates is constant.
#   - put(key, value):    O(1) -> Inserting into hash map and moving nodes both take constant time.
# Space Complexity: O(capacity) -> The hash map and doubly linked list store at most 'capacity' nodes.
         