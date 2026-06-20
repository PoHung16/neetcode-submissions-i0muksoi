"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""
"""
class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next
""" 
# Keywords: LinkedList Cycle -> Fast/Slow pointer
# Image : while fast and fast.next to traverse linkedlist to check cycle with 'slow', 'fast'. Return List head

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
# Time complexity: O(N) ... Traverse size N LinkedinList
# Space complexity:  O(2)....create constant variable

def test():
    #1.create linkedlist
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    #2. run solution
    sol = Solution()
    result = sol.hasCycle(node1)
    #3. print it out
    print(f"{result}:result ")
if __name__ == "__main__":
    test()










