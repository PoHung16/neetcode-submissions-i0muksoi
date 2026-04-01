class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 【優化】先把 inorder 做成 Hash Map，查找位置變成 O(1)
        # key: 數值, value: 在 inorder 裡的 index
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # 這是一個全域指針，用來標記 "Preorder 目前用到第幾個數字了"
        self.pre_idx = 0
        
        # 定義遞迴函數：負責蓋 "Inorder 範圍從 left 到 right" 的樹
        def dfs(left, right):
            # 【Step 1: 停】(Base Case)
            # 如果範圍不合理 (左邊界超過右邊界)，代表沒東西了
            if left > right:
                return None
            
            # 【Step 2: 抓老大】
            # 從 preorder 拿出當前的根節點數值
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            # 指針往後移，準備給下一個節點用
            self.pre_idx += 1
            
            # 【Step 3: 切割】
            # 在 inorder 裡找到老大的位置 (split point)
            mid = inorder_map[root_val]
            
            # 【Step 4: 叫】(Recursion)
            # 蓋左子樹：範圍是 "目前的左邊界" 到 "老大左邊那一格 (mid-1)"
            root.left = dfs(left, mid - 1)
            
            # 蓋右子樹：範圍是 "老大右邊那一格 (mid+1)" 到 "目前的右邊界"
            root.right = dfs(mid + 1, right)
            
            return root
            
        # 一開始範圍是整個 inorder array (0 到 n-1)
        return dfs(0, len(inorder) - 1)




        