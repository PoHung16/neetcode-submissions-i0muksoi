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
    

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # A. Find Mid
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        # B. Split & Reverse:
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # C. Merge:
        first = head # first half head
        second = prev # second half head
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            first.next= second
            first = tmp1
            second.next = first
            second = tmp2





    
