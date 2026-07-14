"""
 OOD: No
 Constraints: No
 input : TreeNode
 output : int
"""

# Optimal Solution
    # Keyword: Tree problem - "need children's info" -> Bottom-Up DFS
    # Approach: base case -> ask left&right child -> Process & update global variable ->Process and Return Up to your boss
    # Tricks: 
        # Global variable : standard Bottom-Up DFS,  can only return one value up to its parent. The final answer doesn't have to come from the root node
class TreeNode:
    def __init__(self, val=0 , left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self,root:TreeNode)->int:
        res = 0 # Global tracker for the longest path
        def dfs(node: TreeNode) -> int:
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res = max(res, left + right) # The diameter through the current node is left edges + right edges
            return max(left, right) + 1 #Return the height of this subtree up to the parent

        dfs(root)
        return res
            

def test():
    sol = Solution()
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    root1.right.right = TreeNode(4)
    root1.right.left.left = TreeNode(5)
    result = sol.diameterOfBinaryTree(root1)
    print(f"Result: {result}")  # Expected Output: 3 (Path: 5 -> 3 -> 2 -> 4 or 5 -> 3 -> 2 -> 1)

if __name__ == "__main__":
    test()

