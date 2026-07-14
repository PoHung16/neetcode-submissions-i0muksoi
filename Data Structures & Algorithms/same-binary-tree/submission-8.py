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
    # --- Test Case 1: Standard Tree ---
    # Constructing: [1, 2, 3]
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    result = sol.isSameTree(root1,root2)

    print(f"Result:{result}")

if __name__ == "__main__":
    test()













