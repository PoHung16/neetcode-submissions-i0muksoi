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
# Keywords: LinkedList Manipulation(Merge/Remove) ->  Dummy LinkedList
# Image: while list to traverse linkedlist and build the list with 'dummy head' and 'curr'. Return List head
# Tricks: 
    # Merge  LinkedList situation: 
        # A. Compare: Check which list has the smaller value.
        # B. Link: Connect 'curr.next' to the smaller node 
        # C. Move : move two pointer forward
        # D. Leftovers: Directly attach any remaining list.


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        curr.next = list1 if list1 else list2
        return dummy.next

# Time complexity: O(N1+N2) ... Traverse size N1+N2 LinkedinList
# Space complexity:  O(1)....create constant variable

def test():
    #1.create linkedlist
    l1_node1 = ListNode(1)
    l1_node2 = ListNode(2)
    l1_node1.next= l1_node2
    l2_node1 = ListNode(1)
    l2_node2 = ListNode(3)
    l2_node1.next= l2_node2
    #2. run solution
    sol = Solution()
    l1_node1 = ListNode(1)
    merged_head = sol.mergeTwoLists(l1_node1,l2_node1)
    curr = merged_head
    #3. prin it out
    while curr:
        print(f"{curr.val}", end = " -> " if curr.next else "\n" )
        curr = curr.next


if __name__ == "__main__":
    test()
    
        