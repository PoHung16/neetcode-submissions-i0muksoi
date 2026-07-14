"""
 OOD: No
 Constraints: No
 input : TreeNode
 output : int
"""

# Optimal Solution
    # Keyword: Tree problem - "need children's info" -> Bottom-Up DFS
    # Approach: base case -> ask left&right child ->Process and Return Up to your boss
class TreeNode:
    def __init__(self,val=0,left=None,right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root:TreeNode)->int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1+ max(left_depth,right_depth)
# Time complexity: O(N) ...  Traverse N nodes in a binary tree,
# Space complexity:  O(h)....The memory that store h recursive call
    # O(N) ...Skewed Tree
    # O(logn) ... balanced tree


def test():
    sol = Solution()
    root1 = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), None))
    result = sol.maxDepth(root1)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()













