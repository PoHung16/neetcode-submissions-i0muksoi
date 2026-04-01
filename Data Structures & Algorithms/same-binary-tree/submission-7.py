class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #思路： 看到Binary Tree , 「不需要父節點的資訊，只需要子節點資訊」
        #題型：基本Bottom-Up DFS
        #腦內圖像：慣老闆 你自己不做事，你只負責分派任務給兩個手下 (Left & Right)，然後把他們的成果拿來隨便加一下就交差。
        #Step1:  Edge case :底沒東西
        if not p and not q:
            return True
        if not p or not q:
            return False
        #Step2:  慣老闆不想動沒有base case or偶爾動一下有base case 
        if p.val != q.val:
            return False
        #Step 3: 向手下要結果，回報給真正大老闆
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
      
        return left and right 
        '''
        Time : O(N) …  Traverse N nodes in a binary tree,
        Space: O(h) …The memory that store h recursive call occupies on the call stack, bc it will only execute one side left or right first.
        O(N)...Skewed Tree
        O(logn) … balanced tree
        '''



