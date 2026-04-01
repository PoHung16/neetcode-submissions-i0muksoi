class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #思路 看到Binary Tree , 「需要父節點的資訊，不用子節點資訊」
        #題型：Top-Down DFS with helper function 
        #腦內圖像- preOrder/ Inorder ：冒險者有preorder名單讓我們知道root是哪個，Inorder陣營讓我們知道哪些node在root左邊，哪個node在root右邊

        #Step1: 定義global variable - pre_idex + in_map
        pre_idx = 0 
        in_map = {val: i for i, val in enumerate(inorder)}

        # Step 2: 定義dfs(left,right)
        def dfs(left, right):
            nonlocal pre_idx
            # Step2-1: Edge case +base case:  走到底了，冒險結束+每一層要做的事
            if left > right:
                return None
            root_val = preorder[pre_idx] #當前的根節點數值
            root = TreeNode(root_val)
            mid = in_map[root_val] #在 inorder 地圖中找到 Root 的位置，用來切分左右

            #Step 2-2:更新gloval variable
            pre_idx += 1 # 跳下一號才知道下一個要create哪個node
            
            # Step 2-3: 繼續往左、往右創造node +回傳node因為要build
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            
            return root

        #Step 3: Call dfs +回傳結果  
        return dfs(0, len(inorder) - 1)

        '''
        Time : O(N) …  Traverse N nodes in a binary tree,
        Space: O(N)
        O(N)... Create Size N Map
        O(N) …The memory that store N recursive call occupies on the call stack, bc it will only execute one side left or right first.
            O(N)...Skewed Tree
            O(logn) … balanced tree

        '''







