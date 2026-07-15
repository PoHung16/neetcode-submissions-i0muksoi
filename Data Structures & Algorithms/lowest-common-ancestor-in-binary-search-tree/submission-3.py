"""
 OOD: No
 Constraints: No
 input : TreeNode, TreeNode
 output : TreeNode
"""
# Binary Search Tree: Tree Left is always smaller; right is always larger.
# Optimal Solution
    # Keyword: Tree Search problem  - "Process from the top, no need children's info" -> Top Down DFS Search
    # Approach: base case -> current node work -> delegate to left&right child
    # Tricks
        # Since it's a BST, we don't need to search both sides. We just check the values and choose one direction to delegate, and only need to return the answer from the one side
class TreeNode:
    def __init__(self,val=0,left= None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q:TreeNode):
        if not root:
            return None
        if not p or not q:
            return None
        if p.val > root.val and q.val > root.val:
            right = self.lowestCommonAncestor(root.right,p,q) # Delegate to Right Child Only 
            return right #only need to return answer from right side
        if p.val < root.val and q.val < root.val:
            left = self.lowestCommonAncestor(root.left,p,q) # Delegate to Left Child Only
            return left
        return root

# Time complexity: O(h) ...  Traverse h nodes in a binary tree,
    # O(N) ...Skewed Tree
    # O(logn) ... balanced tree
# Space complexity:  O(h)....The memory that store h recursive call
    # O(N) ...Skewed Tree
    # O(logn) ... balanced tree
 
 
def test():
    sol = Solution()
    root = TreeNode(5)
    root.left =TreeNode(3, TreeNode(1), TreeNode(4))
    root.right = TreeNode(8, TreeNode(7), TreeNode(9))
    p = TreeNode(3)
    q = TreeNode(4)
    result = sol.lowestCommonAncestor(root,p,q)

    print(f"Result:{result}")

if __name__ == "__main__":
    test()


