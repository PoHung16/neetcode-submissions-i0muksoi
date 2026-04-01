from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Step 0
        if not root:
            return []
            
        # 【動作 1: 進】
        queue = deque([root])
        res = []
        
        while queue:
            # 【動作 2: 鎖】
            # 拍照存證：這一層有幾個人
            level_size = len(queue)
            
            # 【動作 3: 辦】
            for i in range(level_size):
                node = queue.popleft()
                
                # --- 唯一的差別在這裡 ---
                # 如果我是這一層的最後一個 index (i == n-1)
                # 代表我站在最右邊 (從右邊只看得到我)
                if i == level_size - 1:
                    res.append(node.val)
                # ---------------------
                
                # 依然要把小孩加進去，因為下一層還是要看全部
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return res