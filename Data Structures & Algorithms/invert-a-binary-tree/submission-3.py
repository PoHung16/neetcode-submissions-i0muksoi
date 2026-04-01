class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #思路： 看到Binary Tree , 「不需要父節點的資訊，也不用子節點資訊」
        #題型：基本Top-Down DFS 
        #腦內圖像：冒險者一路往下衝
        #Step1:  Edge case: 走到底了，冒險結束
        if not root:
            return 
        #Step2:  Base case : 每一層要做的事
        root.left, root.right = root.right, root.left
        #Step3: 繼續往左、往右衝: dfs(node.left), dfs(node.right)
        self.invertTree(root.left)
        self.invertTree(root.right)
        #Step 4: 回傳結果
        return root
