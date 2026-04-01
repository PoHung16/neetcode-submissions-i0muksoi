class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # 定義一個內部 DFS 函數
        def dfs(node):
            # 【動作 1：停】(Stop)
            # 空節點高度為 0，且絕對平衡
            if not node:
                return 0
            
            # 【動作 2：叫】(Call)
            # 慣老闆先問左右手下
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 【動作 2.5：判】(Check - The Trick)
            # 這裡就是變形的地方！
            # 情況 A: 下屬已經回報爛掉了 (-1) -> 我也跟著爛
            # 情況 B: 下屬沒爛，但我自己左右不平衡 (>1) -> 我宣佈爛掉
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            
            # 【動作 4：算】(Compute)
            # 如果一切平安，就跟以前一樣，回報高度
            return max(left, right) + 1
            
        # 最後只要看根節點有沒有回報 -1 就能知道整棵樹的狀態
        return dfs(root) != -1


        