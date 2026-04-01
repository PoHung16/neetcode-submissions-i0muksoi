class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 準備倉庫 (Stack) 和車子 (cur)
        stack = []
        cur = root
        
        # 只要車子還有油 (cur) 或 倉庫還有貨 (stack)，就繼續跑
        while stack or cur:
            
            # 【Step 1: 鑽到底】(Drill Left)
            # 一直往左開，沿路把經過的點都存進 Stack
            # 目的是為了找到 "目前剩下節點中最小的"
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # 【Step 2: 報數】(Report)
            # 沒路走了，從 Stack 拿出最後一個進去的人 (也就是最小的)
            cur = stack.pop()
            
            # 報數：k 減 1
            k -= 1
            # 如果 k 歸零，代表這就是第 k 小的人 -> 找到了！
            if k == 0:
                return cur.val
            
            # 【Step 3: 轉向】(Turn Right)
            # 這個點處理完了，換處理比它 "稍微大一點點" 的人 (右小孩)
            cur = cur.right
            
        return -1 # 題目保證 k 有效，理論上不會走到這