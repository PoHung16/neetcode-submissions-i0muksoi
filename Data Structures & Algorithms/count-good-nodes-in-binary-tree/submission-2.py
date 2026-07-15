"""
 OOD: No
 Constraints: No
 input : TreeNode
 output : int
"""

# Optimal Solution
    # Keyword: Tree problem - "Process from the top, no need children's info, but need parent's info" -> Top Down DFS with extra parameter
    # Approach: base case -> current node work -> delegate to left&right child
class TreeNode:
    def __init__(self, val=0 , left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            # Base Case
            if not node:
                return 0
            
            # current node work : Check if the current node is "good", node.val need to >= all the ancestor
            is_good = 0
            if node.val >= max_so_far:
                is_good = 1
                max_so_far = node.val # Update the max value for the path going forward

            # 3. Delegate to Children: Hand down the max_so_far to both paths
            left_count = dfs(node.left, max_so_far)
            right_count = dfs(node.right, max_so_far)
            
            # 4. Return total count(including itslef)
            return is_good + left_count + right_count
        
        # 啟動：根節點的門檻就是它自己 (或是負無窮大也可以)
        return dfs(root, root.val)


def test():
    sol = Solution()
  
    root = TreeNode(2)
    root.left = TreeNode(1, TreeNode(3))
    root.right = TreeNode(1, TreeNode(1), TreeNode(5))
    
    result = sol.goodNodes(root)
    print(f"Result: {result}")  # Expected: 3 (Nodes 2, 3, and 5 are good)
    assert result == 3

if __name__ == "__main__":
    test()