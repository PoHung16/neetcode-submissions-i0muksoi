
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

# Keyword :  "Reverse Linked List" -> Basic LinkedList
# Image : while curr to travser linkedlist and flip with 'prev', 'curr'. Return List head
# Tricks: SFM
    # Save: 'temp' save 'curr.next'
    # Flip: 'curr' point backward to 'prev'
    # Move : Move 2 pointer forward

class Solution:
    def reverseList(self, head: ListNode)->ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Time complexity: O(N) ... Traverse size N LinkedinList
# Space complexity:  O(1)....create constant variable

def test():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2

    sol = Solution()
    reverse_head = sol.reverseList(node1)
    curr = reverse_head
    while curr:
        print(f"{curr.val}", end = " ->" if curr.next else "\n")
        curr = curr.next

if __name__ == "__main__":
    test()








        

















