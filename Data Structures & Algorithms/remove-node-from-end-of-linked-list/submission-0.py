class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Step1: 初始化 Dummy Node,  建立兩個指針 Ahead, Behind 指向 dummy。Ahead先走n+1步，保持距離n+1
        dummy = ListNode(0)
        dummy.next = head
        ahead = behind = dummy
        for _ in range(n + 1):
            ahead = ahead.next

        # Step 2:  while ahead 同時開始遍兩個鏈表
        # 當 Ahead 走到 None (終點外) 時，Behind 會停在目標節點的前一個
        while ahead:
            ahead = ahead.next
            behind = behind.next

        # Step 3: 執行刪除動作 (Behind 就在目標的前一格)
        # 動作：把目標節點「跳過去」
        behind.next = behind.next.next

        # Step 4: 回傳結果 (Return dummy.next)
        return dummy.next