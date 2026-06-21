"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Keywords: LinkedList Manipulation(Merge/Remove/Reorder/Copy) ->  Dummy LinkedList
# Image: while list to traverse linkedlist and build the list with 'dummy head' and 'curr'. Return List head
# Tricks: 
    # Merge  LinkedList situation: 
        # A. Compare: Check which list has the smaller value.
        # B. Link: Connect 'curr.next' to the smaller node 
        # C. Move : move two pointer forward
        # D. Leftovers: Directly attach any remaining list.
    # Reorder LinkedList situation: 
        # A. Find Mid: Fast/Slow pointers to find the middle.
        # B. Split & Reverse: Cut at mid (slow.next=None), then reverse 2nd half.
        # C. Merge: Interleave nodes from both halves one by one.
    # Remove Nth From End situation:
        # A. Gap Creation: Move 'fast' pointer n + 1 steps ahead first than 'slow' pointer.
        # B. Sync Move: Move 'fast' and 'slow' together until 'fast' hits None.
        # C. Delete: Skip the target node using slow.next = slow.next.next.
    # Copy List with Random Pointer situation:
        # A. Map Creation: Use a hash map 'old_to_new = {None: None}' to bond original nodes with their clones.
        # B. Phase 1 (Clone Nodes): Traverse the list to create new nodes with 'val' only, and save them in the map.
        # C. Phase 2 (Connect Pointers): Traverse again. Connect 'new.next = old_to_new[old.next]' and 'new.random = old_to_new[old.random]'.
    
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # 用哈希表建立【老节点 -> 新节点】的映射关系
        # 预先放入 None: None，处理当 next 或 random 指向空的情况
        old_to_new = {None: None}
        
        # ==========================================
        # Step 1: 第一遍遍历，把所有新节点创建出来，存入哈希表
        # ==========================================
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val) # 只复制值，指针先空着
            curr = curr.next
            
        # ==========================================
        # Step 2: 第二遍遍历，根据哈希表的映射，把新节点的指针连起来
        # ==========================================
        curr = head
        while curr:
            new_node = old_to_new[curr]
            
            # 新节点的 next，要指向老节点 next 对应的新分身
            new_node.next = old_to_new[curr.next]
            
            # 新节点的 random，要指向老节点 random 对应的新分身
            new_node.random = old_to_new[curr.random]
            
            curr = curr.next
            
        # 返回老头节点 head 对应的新头节点
        return old_to_new[head]
# Time Complexity:  O(N) 
    # Two passes over the list of size N. 
    # Pass 1 clones nodes, Pass 2 connects pointers.
# Space Complexity: O(N) 
    # The hash map stores N 'old_node: new_node' pairs  to track mapping for the deep copy.


def test():
    # 1. 建立 2 个节点: 10 -> 20
    n1, n2 = Node(10), Node(20)
    n1.next = n2
    n1.random = n2  # 10 的 random 指向 20
    n2.random = n1  # 20 的 random 指向 10

    # 2. 跑 Clone
    sol = Solution()
    clone = sol.copyRandomList(n1)

    # 3. 一行打印验证结果 (打印新链表的 val 和 random 的 val)
    print("Original Head:", n1.val, "-> Random:", n1.random.val)
    print("Cloned Head:  ", clone.val, "-> Random:", clone.random.val)
    print("Is same object?", n1 == clone)  # 必须是 False 才是真正的深拷贝

if __name__ == "__main__":
    test()

