class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #思路： 看到Binary Tree , 「不需要父節點的資訊，只需要子節點資訊」
        #題型：基本Bottom-Up DFS

        #Step1:  Edge case :如果 root 是空，回傳 0 或 None。
        if not root:
            return 0
        #Step2:  慣老闆不想動沒有base case:
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        #Step 3: 向手下要結果，回報給真正大老闆
        return 1+max(left,right)







