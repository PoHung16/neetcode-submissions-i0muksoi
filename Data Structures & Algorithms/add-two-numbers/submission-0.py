"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""
"""
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
"""
# Keywords: LinkedList Manipulation(Merge/Remove/Reorder) ->  Dummy LinkedList
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
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0  # 进位数 (不是 0 就是 1)
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # 如果 l1 走完了，就当成 0
            val2 = l2.val if l2 else 0  # 如果 l2 走完了，就当成 0
            total = val1 + val2 + carry
            carry = total // 10         # 计算新的进位 (e.g., 12 // 10 = 1)
            out_val = total % 10        # 计算当前位留在新节点的值 (e.g., 12 % 10 = 2)
        # 新建节点并连接，然后 curr 指针后移
            curr.next = ListNode(out_val)
            curr = curr.next
            # l1 和 l2 指针各自后移 (要先判断是否为空)
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next

# Time complexity: O(N) ... Traverse size N LinkedinList
# Space complexity:  O(1)....create constant variable

def test():
    #1.create linkedlist
    l1_node1 = ListNode(1)
    l1_node2 = ListNode(2)
    l1_node3 = ListNode(3)
    l1_node1.next= l1_node2
    l1_node2.next= l1_node3
    l2_node1 = ListNode(4)
    l2_node2 = ListNode(5)
    l2_node3 = ListNode(6)
    l2_node1.next= l2_node2
    l2_node2.next= l2_node3


    #2. run solution
    sol = Solution()
    new_head = sol.addTwoNumbers(l1_node1,l2_node1)
    curr = new_head
    #3. prin it out
    while curr:
        print(f"{curr.val}", end = " -> " if curr.next else "\n" )
        curr = curr.next


if __name__ == "__main__":
    test()











