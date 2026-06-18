
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
# Image : Initialize prev, curr pointers, while curr traverse linkedlist, save next node, reverse current node, move 2 pointers, , return list head
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
# Space complexity:  O(N)....create constant variable

def test():
    # 1. Create a simple linked list manually: 1 -> 2
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2  # Link them up
    print("Original: 1 -> 2")
    # 2. Run your function
    sol = Solution()
    reversed_head = sol.reverseList(node1)
    # 3. Print the result by walking through the reversed list
    print("Reversed: ", end="")
    curr = reversed_head
    while curr:
        print(curr.val, end=" -> " if curr.next else "\n")
        curr = curr.next
if __name__ == "__main__":
    test()








        

















