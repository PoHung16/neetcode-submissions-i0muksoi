"""
 OOD: No
 Constraints: No
 input : ListNode, int
 output : ListNode
"""

# Keywords: LinkedList Manipulation(Merge/Remove/Reorder) ->  Dummy LinkedList
# Image: while list to traverse linkedlist and build the list with 'dummy head' and 'curr'. Return List head
# Tricks: 
    # Remove Nth From End situation:
        # ps. remove list, you will need to start from dummy node since otherwise you cannot delete head node
        # A. Gap Creation: Move 'fast' pointer n + 1 steps ahead first  with for loop
        # B. Sync Move: Move 'fast' and 'slow' together until 'fast' hits None. Slow will stop at Nth Node From End of List bc the gap is N
        # C. Delete: Skip the target node using slow.next = slow.next.next.
class ListNode:
    def __init__(self,val=0,next=None):
        self.val= val
        self.next = next

class Solution:
    def removeNthFromEnd(self,head:ListNode,n:int)->ListNode:
        dummy = ListNode(0)
        dummy.next= head
        fast = dummy
        slow = dummy
        for _ in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next= slow.next.next

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
    



    


