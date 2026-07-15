"""
 OOD: No
 Constraints: No
 input : TreeNode
 output : List[int]
"""
# Optimal Solution
    # Keyword: Tree Search problem  - "Level by level" -> BFS with a Queue
    # Approach: base case -> Initialize Queue -> Measure Level Size -> Process Current Level -> Queue Up the Next Level
    # Tricks:
        # If it's the last node in the current level, it's visible from the right!

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode)-> List[int]:
        if not root: 
            return[]
        res = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size-1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

# Time complexity: O(N) ...  Traverse N nodes in a binary tree - one side,
# Space complexity:  O(N)... the worst case - perfect binary tree, N/2 in bottom level
 
def test():
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(4))
    root.right = TreeNode(3, None, TreeNode(5))
    
    result = sol.rightSideView(root)
    print(f"Result: {result}")  # Expected: [1, 3, 5]
    assert result == [1, 3, 5]

if __name__ == "__main__":
    test()

