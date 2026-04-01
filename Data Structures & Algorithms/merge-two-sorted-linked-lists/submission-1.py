# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #思路： 看到LinkedList Merge/Remove/Reorder/Partition -  Dummy Node 題型
        #題型： Dummy Node 題型
        #Step1: 初始化 Dummy Node,  建立一個指針 curr 指向 dummy
        dummy = ListNode(0)
        curr = dummy
        #Step 2:  while list1 and list2 同時開始遍兩個鏈表
        while list1 and list2:
            #Step 2-1: 比較大小，把較小的接在 curr 後面. 
            #Step 2-2: curr 要往後移到list 1 or list 2, list1 or list 2也往後
            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        #Step 3:  cur.next 接上剩下的list
        curr.next = list2 if list2 else list1
        #Step 4:回傳head
        return dummy.next
        