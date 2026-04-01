# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        #思路： 看到Binary Tree / Binary Search Tree
        #題型：基本Top-Down DFS : 不是BST，不是分層，處理「從根節點開始」的路
        #Step1:  定義global variable
        res = 0
        #Step2:  定義dfs(node, parent, 目前情況)
        def dfs(node,parent,current_len):
            nonlocal res
            #Step2-1: Edge case: 走到底了，冒險結束
            if not node:
                return
            #Step2-2 :Base case : 每一層要做的事，並更新gloval variable
            if node.val == parent + 1:
                current_len += 1
            else:
                current_len = 1
            res = max(res,current_len)
            #Step2-3 : 繼續往左、往右衝
            dfs(node.left,node.val,current_len)
            dfs(node.right,node.val,current_len)

        #Step 3: Call dfs - 這題有個小trick第一個節點沒有爸爸，所以傳個讓它會變 1 的值 
        dfs(root, root.val -1, res)
        #Step 4: 回傳結果
        return res


        