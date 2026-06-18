"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
# Keyword :  "Merge/Remove/Reorder/Partition LinkedList" -> DummyNode LinkedList
# Image : Initialize redummy node, curr pointers, while list traverse linkedlist, and do following,  move 2 pointer, return list head
# Tricks: 
    # Merge  LinkedList situation: 
        # A. Compare 2 LinkedList value , connect linkedlist wiht smaller value one
        # B. Connect with the leftover list


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
        curr.next = list2 if list2 else list1
        return dummy.next
        

        