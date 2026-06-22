"""
 OOD: No
 Constraints: No
 input : ListNode, int
 output : ListNode
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
        # ps. remove list, you will need to start from dummy node since otherwise you cannot delete head node
        # A. Gap Creation: Move 'fast' pointer n + 1 steps ahead first than 'slow' pointer with for loop
        # B. Sync Move: Move 'fast' and 'slow' together until 'fast' hits None.
        # C. Delete: Skip the target node using slow.next = slow.next.next.
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        # Step 1: Fast 先走 n + 1 步 , 目的是让 fast 和 slow 之间保持 n 个节点的内部间距
        for _ in range(n+1):
            fast = fast.next
        # Step 2: Fast 和 Slow 同时前进，slow 刚好停在“倒数第 n 个节点”的「前驱节点」(距離結尾n格位置)
        while fast:
            fast = fast.next
            slow = slow.next
        # Step 3: 跨过倒数第 n 个节点（删除操作）
        slow.next = slow.next.next  
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
    #2. run solution
    sol = Solution()
    remove_head = sol.removeNthFromEnd(l1_node1,2)
    curr = remove_head
     #3. prin it out
    while curr:
        print(f"{curr.val}", end = " -> " if curr.next else "\n" )
        curr = curr.next

if __name__ == "__main__":
    test()
    



    


