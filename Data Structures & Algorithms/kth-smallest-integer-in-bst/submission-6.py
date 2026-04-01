class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #思路： 看到Binary Tree , 「需要父節點的資訊」
        #題型：Top-Down DFS with helper function - Inorder Traversal
        #腦內圖像：冒險者帶著背包一路往下衝，把沿路看到的資訊塞進包包（current_length),並更新global variable
        #Ps.此題需要父節點的k資訊，但因為小孩也會改動到k, 所以我們用global variable代傳
        
        #Step1:  定義global variable
        res = None
        count = k
        #Step2:  定義dfs(node)
        def dfs(node):
            nonlocal res, count
            #Step2-1: Edge case: 走到底了，冒險結束
            if not node or res is not None:
                return
            #Step2-2 :往左衝: dfs(node.left)
            dfs(node.left)
            #Step2-3 :Base case : 每一層要做的事，並更新global variable
            count -= 1
            if count == 0: #代表找到了第k小
                res = node.val
            #Step2-3 : 往右衝: dfs(node.right)
            dfs(node.right)
        #Step 3: Call dfs
        dfs(root)
        #Step 4: 回傳結果
        return res
    '''
    Time : O(N) …  Traverse N nodes in a binary tree,
    Space: O(h) …The memory that store h recursive call occupies on the call stack, bc it will only execute one side left or right first.
    O(N)...Skewed Tree
    O(logn) … balanced tree
    '''
            

        
