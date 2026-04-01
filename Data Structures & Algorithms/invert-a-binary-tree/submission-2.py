class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 【動作 1：停】(Stop)
        # 看到空節點，沒事可做，直接回傳
        if not root:
            return None
        
        # 【動作 2：算 / 辦事】(Compute)
        # 慣老闆只負責交換自己手上的這兩個
        root.left, root.right = root.right, root.left
        
        # 【動作 3：叫】(Call)
        # 剩下那些子孫的交換工作，外包給左右小孩自己去煩惱
        # (這裡不需要回傳值，只要叫他們去執行就好)
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 任務完成，交卷
        return root