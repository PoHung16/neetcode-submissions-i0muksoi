class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #思路：看到Binary Tree , 「需要子節點資訊，且需要回報2件事 or function 參數/回傳形態不同」
        #題型： Bottom-UP DFS 題型with helper function
        #腦內圖像：慣老闆 你自己不做事，你只負責分派任務給兩個手下 (Left & Right)，然後把他們的成果拿來隨便加一下就交差.

        #Step1:  定義global variable - no need
        #Step2:  def dfs(node, left, right)
        def dfs(node, left, right):   
            #Step2-1:  Edge case + Base case：
            # Edge Case：處理不尋常的情況
            # Base Case：每層該做的事
            if not node:
                return True
            if not (left < node.val < right):
                return False  
            # Step2-2 :慣老闆不想動叫左右手下去做事,
            # 下限(left)不變，但上限(right) 變成了 "我(node.val)"
            left_child = dfs(node.left, left, node.val) 
            right_child = dfs(node.right, node.val, right)
            
            #Step2-3 :  向手下要結果，回報給真正大老闆
            return left_child and right_child

        #Step 3: Call dfs + 回傳結果
        return dfs(root, float("-inf"), float("inf"))
        
        '''
        Time : O(N) …  Traverse N nodes in a binary tree,
        Space: O(h) …The memory that store h recursive call occupies on the call stack, bc it will only execute one side left or right first.
        O(N)...Skewed Tree
        O(logn) … balanced tree
        '''

