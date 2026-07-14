"""
 OOD: No
 Constraints: No
 input : TreeNode
 output : boolean
"""

# Optimal Solution
    # Keyword: Tree problem - "need children's info" -> Bottom-Up DFS
    # Approach: base case -> ask left&right child -> Process & update global variable ->Process and Return Up to your boss
    # Tricks: 
        # Global variable : standard Bottom-Up DFS,  can only return one value up to its parent. (height)

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root:TreeNode) -> bool:
        res = True
        def dfs(node:rootNode)->int:
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left-right) >1:
                res = False
            return max(left,right)+1
        dfs(root)
        return res


# Time complexity: O(N) ...  Traverse N nodes in a binary tree,
# Space complexity:  O(h)....The memory that store h recursive call
    # O(N) ...Skewed Tree
    # O(logn) ... balanced tree


def test():
    sol = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)

    result = sol.isBalanced(root1)
    print(f"Result: {result}")  # Expected Output: 3 (Path: 5 -> 3 -> 2 -> 4 or 5 -> 3 -> 2 -> 1)

if __name__ == "__main__":
    test()






