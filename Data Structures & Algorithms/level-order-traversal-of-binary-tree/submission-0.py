from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Step 0. 邊界檢查
        if not root:
            return []
            
        # Step 1. 進 (Init)
        # 準備隊伍，先把老大放進去
        queue = deque([root])
        res = []  # 這是最後要交的總表
        
        while queue:
            # Step2. 鎖 (Snapshot)
            # 這一刻，隊伍裡的長度，就是「這一層」的所有人數
            level_size = len(queue)
            current_level = []  # 用來裝這一層的數字
            
            # Step3. 掃 (
            # 我們只處理鎖定的這 level_size 個人
            for _ in range(level_size):
                node = queue.popleft()  # 把人拿出來 (pop)
                current_level.append(node.val)  #  記下來 
                
                # 叫小孩去後面排隊 (下一層)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # 這一層辦完了，整包放進結果
            res.append(current_level)
            
        return res