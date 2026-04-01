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
        #Step1: Deal with the original node
        # Put the original node & its clone node in visited Map
        #Put the original node into the queue for processing its neighbor

        visited = {
            node : Node(node.val)
        }
        queue = deque([node])
        # Step2: Process Queue for BFS
        while queue:
            # 2-A 拿出original node
            curr = queue.popleft()
            # 2-B Traverse original node的所有鄰居
            for neighbor in curr.neighbors:
                # 2-B-1 Deal with the original neighbor node
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # 2-B-2 Connect the clone original node & clone neighbor together
                visited[curr].neighbors.append(visited[neighbor])
        #Step 3 : Return result        
        return visited[node]


# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V)....create size V Map and size V queue



