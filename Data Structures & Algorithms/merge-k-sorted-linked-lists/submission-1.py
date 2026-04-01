import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #動作記憶法和步驟-Heap 題型：
        #Step 1:  初始化一個空的 Min-Heap
        min_heap = []
        #Step 2:  Iterate over array to build heap
        for i, node in enumerate(lists):
            if node:
                #我們把每一條 List 的 第一個節點 丟進堆裡。
                #丟進去的東西是一個元組 (Tuple)：(節點的值, 它是第幾個 List, 節點本人)
                #為什麼要放 i？ 因為如果兩個節點的值（node.val）一模一樣，Python 的 Heap 會去比較下一個元素。如果不放 i，它會直接比較 ListNode 物件，而 ListNode 不支援比較運算，程式會 Crash。
                heapq.heappush(min_heap, (node.val, i, node))
        #動作記憶法和步驟-Dummy Node 題型
        #Step1: 初始化 Dummy Node
        dummy = ListNode(0)
        #Step 2: 建立一個指針 curr，指向 dummy 開始移動
        curr = dummy
        #Step 3:  while heap同時開始遍k個鏈表
        while min_heap:
            #Step 3-1: 比較大小，把較小的接在 curr 後面. 
            val, i , node = heapq.heappop(min_heap)
            curr.next = node
            #Step 3-2: curr 要往後移到list 1 or list k, list1 or list k也往後移
            curr = node
            node = node.next
            #Step3-3: 還有node要放到heap在排序一次
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        #Step 4:回傳head
        return dummy.next














