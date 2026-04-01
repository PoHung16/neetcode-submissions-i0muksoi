# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Ps.看有沒有edge case, return false
        if not head:
            return False
        #Step1: 初始化fast, slow pointer
        fast = head
        slow = head
        #Step 2: While fast and fast.next開始遍地
        while fast and fast.next:
            #Step 2-1: slow = slow.next
            slow = slow.next
            #Step 2-2: fast = fast.next.next
            fast = fast.next.next
            #Step 2-3:  If slow == fast return True
            if slow == fast:
                return True
        return False