class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 這裡的 valid 就是我們的 DFS 遞迴函數
        # node: 當前檢查的節點
        # left: 最小值邊界 (不能比這個小)
        # right: 最大值邊界 (不能比這個大)
        def valid(node, left, right):
            
            # 【步驟 1：停】(Stop)
            # 遇到空節點 -> 代表這條路檢查到底了，沒問題 -> 通過
            if not node:
                return True
            
            # 【步驟 1.5：判】(Check)
            # 邊境檢查：拿出你的證件 (node.val)
            # 看看你有沒有乖乖待在 (left, right) 之間？
            if not (left < node.val < right):
                return False  # 抓到了！違規！
            
            # 【步驟 2：叫】(Call)
            # 我自己檢查過了，換檢查我的左右小孩
            # 這裡是最關鍵的 "參數下傳"：

            # 下限(left)不變，但上限(right) 變成了 "我(node.val)"
            # (左小孩：你不准比爸爸大！)
            left_child = valid(node.left, left, node.val) 

             # 下限(left) 變成了 "我(node.val)"，上限(right)不變
                # (右小孩：你不准比爸爸小！)
                #只要比爸爸大就好，沿用祖先的上限
            right_child = valid(node.right, node.val, right)
            
            return (left_child and  right_child)

        # 一開始，範圍是無限大 (-inf 到 +inf)
        return valid(root, float("-inf"), float("inf"))

