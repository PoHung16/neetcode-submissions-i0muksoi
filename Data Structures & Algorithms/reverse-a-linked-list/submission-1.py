# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #Step1:  初始化指針 - prev, curr
        prev = None
        curr = head
        #Step2:  while curr 開始遍地
        while curr:
            #Step 2-1: 先存下原本的下一步，不然斷掉後會找不到人
            temp = curr.next 
            #Step 2-2: 反轉指向
            curr.next = prev
            #Step 2-3:  prev, curr 向前移動
            prev = curr
            curr = temp
        #Step 3:回傳head
        return prev


        

















