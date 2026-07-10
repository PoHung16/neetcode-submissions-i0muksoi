"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""

# Optimal Solution
    # Keyword: LinkedList Manipulation(Merge/Remove/Reorder) ->  Dummy LinkedList
    # Approach: Use 'dummy head' and 'curr' pointer , the while list to traverse linkedlist
# Tricks: 
    # Reorder LinkedList situation: 
        # A. Find Mid: Fast/Slow pointers to find the middle.
        # B. Split : Cut at mid (slow.next=None)
        # C. Reverse: prev & curr pointer -> while curr -> Move pointer direction, then move pointer
        # D. Merge: first & second pointer -> while first and second -> Move pointer direction, then move pointer
        
    











        # D. Merge: Interleave nodes from both halves one by one.
    # Merge LinkedList situation: 
        # A. while first and second  -> Move pointer direction, then move pointer
        # B. Attach Leftover

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head:ListNode) -> None:
        # Find mid
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None

        # Reverse
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Merge
        first = head
        second = prev

        while first and second:
            nxt1 = first.next
            nxt2 = second.next
            first.next = second
            first = nxt1
            second.next = first
            second = nxt2







           
            
            
           
            
            

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
    sol.reorderList(l1_node1)
    curr = l1_node1
    #3. print it out
    while curr:
        print(f"{curr.val}", end= "->" if curr.next else "\n")
        curr = curr.next

if __name__ == "__main__":
    test()
    



    
