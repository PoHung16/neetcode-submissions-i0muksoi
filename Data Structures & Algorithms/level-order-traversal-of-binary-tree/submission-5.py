"""
 OOD: No
 Constraints: No
 input : TreeNode
 output : List[List[int]]
"""
# Optimal Solution
    # Keyword: Tree Search problem  - "Level by level" -> BFS with a Queue
    # Approach: base case -> Initialize Queue -> Measure Level Size -> Process Current Level -> Queue Up the Next Level

class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root:TreeNode)-> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            level_size = len(queue)# Number of nodes on the current level
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                #  Queue Up the Next Level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(current_level)
        
        return res

# Time complexity: O(N) ...  Traverse N nodes in a binary tree - one side,
# Space complexity:  O(N)... the worst case - perfect binary tree, N/2 in bottom level
 






