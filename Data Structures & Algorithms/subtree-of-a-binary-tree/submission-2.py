# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #思路： 看到Binary Tree , 「不需要父節點的資訊，只需要子節點資訊」
        #題型：基本Bottom-Up DFS
        #腦內圖像：慣老闆 你自己不做事，你只負責分派任務給兩個手下 (Left & Right)，然後把他們的成果拿來隨便加一下就交差。
        #Step1:  Edge case 底沒東西
        if not root:
            return False
        if not subRoot:
            return True
        #Step2: 慣老闆不想動沒有base case or偶爾動一下有base case 叫左右手下去做事
        if self.isSameTree(root,subRoot):
            return True
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)
        #Step 3: 向手下要結果，回報給真正大老闆
        return left or right
        

    def isSameTree(self,rootA,rootB) -> bool:
        if not rootA and not rootB:
            return True
        if not rootA or not rootB:
            return False
        if rootA.val != rootB.val:
            return False
        left = self.isSameTree(rootA.left,rootB.left)
        right = self.isSameTree(rootA.right,rootB.right)
        return left and right

        