class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #思路： 看到Binary Tree , 「需要父節點的資訊」
        #題型：Top-Down DFS with helper function - Inorder Traversal
        #腦內圖像：冒險者帶著背包一路往下衝，把沿路看到的資訊塞進包包（current_length),並更新global variable
        #Ps.此題需要父節點的k資訊，但因為小孩也會改動到k, 所以我們用global variable代傳
        res = None
        count = k
        def dfs(node):
            nonlocal res, count
            if not node or res is not None:
                return
            dfs(node.left)
            count -= 1
            if count == 0: #代表找到了第k小
                res = node.val
            dfs(node.right)

        dfs(root)
        return res

            
            

        
