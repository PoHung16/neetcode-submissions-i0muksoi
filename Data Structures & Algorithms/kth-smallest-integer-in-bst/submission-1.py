class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 思路：中序遍歷 (左 -> 根 -> 右)
        # 我們需要兩個變數：一個存答案，一個存目前數到第幾個
        self.k = k
        self.res = None
        
        def inorder(node):
            if not node or self.res is not None:
                return
            
            # 1. 往左走 (找更小的)
            inorder(node.left)
            
            # 2. 處理當前節點 (數數看)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            
            # 3. 往右走
            inorder(node.right)
            
        inorder(root)
        return self.res