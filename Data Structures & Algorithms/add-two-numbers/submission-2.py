"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""

# Keywords: LinkedList Manipulation(Merge/Remove/Reorder/Add Two Number) ->  Dummy LinkedList
# Image: while list to traverse linkedlist and build the list with 'dummy head' and 'curr'. Return List head
# Tricks
    # LinkedList Add Number Situaion
        # Step1: while l1 or l2 or carry to traverse the list
        # Step2: store out_val in new node, curr.next point to new node
        # Step3: l1, l2 move forward

class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            out_val = total % 10
            curr.next = ListNode(out_val)
            curr = curr.next
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 
        return dummy.next


# Time complexity: O(N) ... Traverse 2 size N LinkedinList
# Space complexity:  O(1)....create constant variable

def test():
    #1.create linkedlist
    l1_node1 = ListNode(7)
    l1_node2 = ListNode(2)
    l1_node3 = ListNode(3)
    l1_node1.next= l1_node2
    l1_node2.next= l1_node3
    l2_node1 = ListNode(9)
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











