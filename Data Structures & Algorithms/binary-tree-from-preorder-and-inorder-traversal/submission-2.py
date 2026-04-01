class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #思路 看到Binary Tree , 「需要父節點的資訊」，這沒辦法背題型！
        #題型：Top-Down DFS with helper function l  - Inorder Traversal +  Preorder Traversal
        #腦內圖像：冒險者帶著背包一路往下衝，把沿路看到的資訊塞進包包（current_length),並更新global variable
        #Step1:  定義global variable
        #preorder = [3,9,20,15,7]
        #inorder = [9,3,15,20,7]
        #讓我們知道root是哪個,我們現在要create哪個node
        pre_idx = 0 
        #讓我們知道哪些node在root左邊，哪個node在root右邊
        in_map = {val: i for i, val in enumerate(inorder)}

        # Step 2: 定義 dfs(left, right) -> 帶著「邊界背包」往下衝
        # left, right 代表目前這棵子樹在 inorder 陣列中的範圍，由父節點獲得
        def dfs(left, right):
            nonlocal pre_idx
            
            # Step 2-1: Edge case (範圍縮小到沒了，代表這條路走到底了)
            if left > right:
                return None

            # Step 2-2: Base case (每一層要做的事：建立節點)
            root_val = preorder[pre_idx] #當前的根節點數值
            pre_idx += 1 # 跳下一號才知道下一個要create哪個node
            mid = in_map[root_val] #在 inorder 地圖中找到 Root 的位置，用來切分左右
            root = TreeNode(root_val)

            # Step 2-3: 繼續往左、往右衝 (切出新邊界)
            # 左子樹的範圍：爸爸的左邊界 到 Root 的左一格
            root.left = dfs(left, mid - 1)
            # 右子樹的範圍：Root 的右一格 到 爸爸的右邊界
            root.right = dfs(mid + 1, right)
            
            return root

        # Step 3 & 4: Call and Return
        return dfs(0, len(inorder) - 1)