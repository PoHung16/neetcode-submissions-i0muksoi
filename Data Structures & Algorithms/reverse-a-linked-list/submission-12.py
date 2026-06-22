
"""
 OOD: No
 Constraints: No
 input : ListNode
 output : ListNode
"""
# Keyword :  "Reverse Linked List" -> Reverse LinkedList
# Image : while curr to traverse linkedlist and flip with 'prev', 'curr'. Return List head
# Tricks: Reverse Situation
    # Save: 'temp' save 'curr.next'
    # Flip: 'curr' point backward to 'prev'
    # Move : Move 2 pointer forward
class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head:ListNode)-> ListNode:
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

# Time complexity: O(N) ... Traverse size N LinkedinList
# Space complexity:  O(1)....create constant variable

def test():
    #1.create linkedlist
    node1 = ListNode(1)
    node2 = ListNode(2)     
    node3 = ListNode(3)     
    node1.next = node2
    node2.next = node3
    #2. run solution
    sol = Solution()
    reverse_head = sol.reverseList(node1)
    curr = reverse_head
    #3. print it out
    while curr:
        print(f"{curr}", end= "->" if curr.next else "\n")
        curr = curr.next

if __name__ == "__main__":
    test()

















        

















