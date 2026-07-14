"""
 OOD: No
 Constraints: No
 input : TreeNode
 output : TreeNode
"""
# Optimal Solution
    # Keyword: Tree problem - "Process from the top, no need children's info" -> Top Down DFS
    # Approach: base case -> current node work -> delegate to left&right child
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root:TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# Time complexity: O(N) ...  Traverse N nodes in a binary tree,
# Space complexity:  O(h)....The memory that store h recursive call
    # O(N) ...Skewed Tree
    # O(logn) ... balanced tree
 
def test():
    sol = Solution()
    # --- Test Case 1: Standard Tree ---
    # Constructing: [1, 2, 3]
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    inverted1 = sol.invertTree(root1)
    
    # Simple direct verification using basic asserts
    assert inverted1.val == 1
    assert inverted1.left.val == 3
    assert inverted1.right.val == 2
    print("Test Case 1 Passed! ✅")

if __name__ == "__main__":
    test()
