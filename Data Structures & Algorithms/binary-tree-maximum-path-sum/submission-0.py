class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 【Step 0: 初始化擂台】
        # 這是全域變數，用來記錄 "歷史最強路徑"
        # 設為負無限大，因為題目節點可能有負數 (例如 [-3])
        self.res = float('-inf')

        def dfs(node):
            # 【Step 1: 停 (Base Case)】
            if not node:
                return 0
            
            # 【Step 2: 問 (Ask)】
            # 遞迴問左右小孩：你們那邊能貢獻多少？
            # 🌟 關鍵細節：如果小孩回報負數，就切斷關係 (取 max 0)，當作沒這條路
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # 【Step 3: 搶 (Update Global) - 私事】
            # 私下結算：以 "我" 為頂點，把左右串起來 (倒 V 字型)
            # 這條路徑只在這裡計算，不會傳給上面 (因為不能分岔)
            current_triangle_sum = node.val + left_gain + right_gain
            
            # 挑戰世界紀錄
            self.res = max(self.res, current_triangle_sum)
            
            # 【Step 4: 報 (Report) - 公事】
            # 回報給爸爸：我只能提供一條腿 (直 I 字型)
            # 選左邊或右邊最大的一條 + 我自己
            return node.val + max(left_gain, right_gain)

        # 【Step 5: 啟動】
        dfs(root)
        
        # 【Step 6: 繳卷】
        return self.res