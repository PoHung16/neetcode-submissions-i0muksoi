# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 把 root 當作現在的車子位置
        if not root:
            return None
        cur = root
        while cur:
            #Step 1 & 2 : 判 & Turn
            # 都在右邊 -> 往右開
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
                
            # 都在左邊 -> 往左開
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
                
            # Step 3: 到 ->分岔了 (一左一右，或撞到其中一個) -> 停車，這裡就是答案
            else:
                return cur




        