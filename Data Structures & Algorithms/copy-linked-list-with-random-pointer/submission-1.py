"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""

# Keyword :  “ Reverse Linked List “ or “Copy Linked List with Random Pointer” -> Basic LinkedList
# Image : while curr to traverse linkedlist and flip with 'prev', 'curr'. Return List head
# Tricks: 
    # Copy List with Random Pointer situation:
        # A. Map Creation: Use a hash map 'old_to_new = {None: None}' to bond original nodes with their clones.
        # B. Phase 1 (Clone Nodes): Traverse the list to create new nodes with 'val' only, and save them in the map.
        # C. Phase 2 (Connect Pointers): Traverse again. Connect 'new.next = old_to_new[old.next]' and 'new.random = old_to_new[old.random]'.

class ListNode:
    def __init__(self, val=0 ,next=None, random= None):
        self.val = val
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head:ListNodee)->ListNode:
        if not head:
            return None
        old_to_new = {None:None}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)  # 只复制值，指针先空着
            curr = curr.next
        
        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next =old_to_new[curr.next]
            new_node.random =old_to_new[curr.random]
            curr = curr.next
    
        return old_to_new[head]

# Time Complexity:  O(N) 
    # Two passes over the list of size N. 
# Space Complexity: O(N) 
    # Create size N hashMap

def test():
    #1.create linkedlist
    node1 = ListNode(0)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node1.next = node2
    node1.random =node3
    node2.next = node3
    node2.random =node1

    #2. run solution
    sol = Solution()
    clone_head = sol.copyRandomList(node1)
    curr = clone_head
    #3. print it out
    while curr:
        print(f"{curr.val}", end =" -> " if curr.next else "\n")
        curr = curr.next


if __name__ == "__main__":
    test()

