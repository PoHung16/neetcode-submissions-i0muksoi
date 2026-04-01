# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_idx = 0
        in_map = {val : in_idx for in_idx, val in enumerate(inorder)}
        def dfs(left,right):
            nonlocal pre_idx
            if left>right:
                return
            rootVal = preorder[pre_idx]
            mid = in_map[rootVal]
            pre_idx +=1
            root = TreeNode(rootVal)

            root.left = dfs(left,mid-1)
            root.right = dfs(mid+1, right)
            return root


        return dfs(0, len(inorder)-1)







