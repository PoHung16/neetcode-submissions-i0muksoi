class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 【動作 1：停】(Stop)
        # 到底了，沒東西就是 0 層
        if not root:
            return 0
        
        # 【動作 2：叫】(Call)
        # 慣老闆不想動，叫左右手下去量他們自己的深度
        # (完全信任他們會回傳一個數字回來)
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        # 【動作 3：算】(Compute)
        # 整理報告：挑比較深的那個，加上我自己 (+1)
        return max(left, right) + 1