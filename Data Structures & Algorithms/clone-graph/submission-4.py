"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 題型Keyword:  “shortest path” or “clone graph”
        # 腦中圖像: “Level by level traverse graph ”
        # 動作記憶法 - 三個步驟
        if not node:
            return None
        #ps.Edge case
        # Step1: Step 1: Put original node /  clone node  in 
        # visited Map/Set
        # Queue for processing its neighbor
        visited_map = {
            node : Node(node.val)
        }
        queue = deque([node])

       # Step2: Process Queue for BFS
        while queue:
            # 2-A Take out the queue node one by one
            curr = queue.popleft()
            # 2-B Traverse all current node’s neighbor and do step 1 and connect all neigbors
            for neighbor in curr.neighbors:
                if neighbor not in visited_map:
                    visited_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited_map[curr].neighbors.append(visited_map[neighbor])
        #Step 3 : Return result        
        return visited_map[node]


# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V)....create size V Map and size V queue



