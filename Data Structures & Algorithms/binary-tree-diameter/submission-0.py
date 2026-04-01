class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 準備一個全域變數 (獎盃)，用來記錄「目前發現的最長路徑」
        res = 0
        
        def dfs(node):
            nonlocal res
            # Base Case: 撞到牆壁 (空節點)，長度是 0
            if not node:
                return 0
            
            # 【動作 1：問】(Ask)
            # 遞迴問左右小孩：「你們單邊最長能延伸多深？」
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # 【動作 2：搶】(Update Global Variable)
            # 這是「私下」做的計算。
            # 試著把左手和右手接起來變成「拱橋」，長度就是 L + R
            # 如果這座橋比之前的紀錄還長，就更新獎盃
            res = max(res, left_height + right_height)
            
            # 【動作 3：報】(Report)
            # 這是「公事公辦」。
            # 回報給你的爸爸：「我這裡最長的一條腿是多長？」
            # 只能選一邊 (max)，然後加上我自己這一段 (+1)
            return 1 + max(left_height, right_height)
            
        # 啟動 DFS
        dfs(root)
        
        # 回傳最後獎盃上的數字
        return res