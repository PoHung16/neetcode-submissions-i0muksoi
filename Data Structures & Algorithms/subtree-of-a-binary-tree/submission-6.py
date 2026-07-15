"""
 OOD: No
 Constraints: No
 input : TreeNode, TreeNode
 output : boolean
"""
# Optimal Solution
    # Keyword: Tree problem - "Process from the top, no need children's info" -> Top Down DFS
    # Approach: base case -> current node work -> delegate to left&right child
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root:TreeNode, subRoot:TreeNode)->bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root,subRoot):
            return True
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)
        return left or right
        
    def isSameTree(self,p:TreeNode, q:TreeNode)->bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
        return left and right


# Time complexity: O(N) ...  Traverse N nodes in a binary tree,
# Space complexity:  O(h)....The memory that store h recursive call
    # O(N) ...Skewed Tree
    # O(logn) ... balanced tree
 
def test():
    sol = Solution()
    root = TreeNode(1)
    root.left =TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3)
    subRoot = TreeNode(2, TreeNode(4), TreeNode(5))
    result = sol.isSubtree(root,subRoot)

    print(f"Result:{result}")

if __name__ == "__main__":
    test()



        