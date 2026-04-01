class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #思路：看到Binary Tree , 「需要子節點資訊，且需要回報2件事 or function 參數/回傳形態不同」
        #題型： Bottom-UP DFS 題型with helper function
        #腦內圖像：慣老闆 你自己不做事，你只負責分派任務給兩個手下 (Left & Right)，然後把他們的成果拿來隨便加一下就交差.
        
        #Step1:  定義global variable 
        res = float('-inf')
        #Step2:  def dfs(node, left, right)
        def dfs(node):
            nonlocal res
            # Step2-1: Edge case + Base case：
            # Edge Case：處理不尋常的情況
            # Base Case：每層該做的事
            if not node:
                return 0
            
            #Step2-2 :慣老闆不想動叫左右手下去做事 (負的就不用算了)
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # Base Case：每層該做的事
            current_triangle_sum = node.val + left + right
            
            # Step2-3 :  update global variable if needed
            res = max(res, current_triangle_sum)
            
            #Step2-4 :  向手下要結果，回報給真正大老闆
            return node.val + max(left, right)

        # Step 3: Call dfs +  回傳結果
        dfs(root)
        return res

        '''
        Time : O(N) …  Traverse N nodes in a binary tree,
        Space: O(h) …The memory that store h recursive call occupies on the call stack, bc it will only execute one side left or right first.
        O(N)...Skewed Tree
        O(logn) … balanced tree
        '''












