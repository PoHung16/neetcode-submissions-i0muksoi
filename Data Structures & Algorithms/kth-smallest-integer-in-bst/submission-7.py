class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #思路： 看到Binary Tree , 「需要父節點的資訊，不用子節點資訊」
        #題型：Top-Down DFS with helper function
        # 腦內圖像- Searh in BST： 冒險者按順序點名，包包裡裝著一個計數器 k。每點到一個人，k 就減 1，當 k 變成 0 的那一刻，眼前那個人就是我們要的答案        
        #Step1:  定義global variable
        res = None
        count = k
        #Step2:  定義dfs(node):不能有其他參數,因為children node還要傳給parent node
        def dfs(node):
            nonlocal res, count
            #Step2-1: Edge case : 走到底了，冒險結束
            if not node or res is not None:
                return
            #Step2-2: 繼續往左衝
            dfs(node.left)
            #Step2-3: base case: 每一層要做的事
            count -= 1
            if count == 0: #代表找到了第k小
                #Step2-4:更新gloval variable
                res = node.val
            #Step2-5 dfs(node.right)
            dfs(node.right)
        #Step 3: Call dfs +回傳結果
        dfs(root)
        return res
        '''
        Time : O(N) …  Traverse N nodes in a binary tree,
        Space: O(h) …The memory that store h recursive call occupies on the call stack, bc it will only execute one side left or right first.
        O(N)...Skewed Tree
        O(logn) … balanced tree
        '''
            

        
