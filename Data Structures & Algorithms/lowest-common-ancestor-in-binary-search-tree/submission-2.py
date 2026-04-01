# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #思路： 看到Binary Search Tree 
        #題型：BST題型
        #腦內圖像：GPS 導航你開著車 (cur)，目標是去某個地址 (target)。 你每到一個路口 (Node)，只做一件事：看路牌比大小，然後轉彎
        #Step1:  Edge case 
        if not root:
            return None
        if not p or not q:
            return None
        curr = root
        #Step2:  GPS 導航你開著車 (cur)，目標是去某個地址 (target) 進行判斷左轉右轉or 分岔(一左一右，或撞到其中一個), 分岔就回傳答案
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr