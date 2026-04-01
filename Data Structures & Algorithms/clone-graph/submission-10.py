"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 題型Keyword:  “shortest path” or “clone graph” -> BFS graph
        # 腦中圖像: “Level by level traverse graph ”, 怕 Stack Overflow：如果圖的深度非常深（例如幾千個節點連成一條線），DFS 可能會導致遞迴深度限制報錯。
        # 動作記憶法 - 4個步驟
        # Edge case:
        if not node:
            return None
        #ps.Decide if its’ a matrix or adjacent list graph - > adjacent list graph
        # Step1: : Build up the graph 
        # visited Map/Set : with original node /  clone node
        # Queue for processing its neighbor
        visited_map = {
            node: Node(node.val)
        }
        queue = deque([node])
        # Step2: Exploring Phase -  Process Queue for BFS - Adjacenet List 
        while queue:
            # 2-A Take out the queue node one by one
            curr = queue.popleft()
             # 2-B Traverse all current node’s neighbor and add to the graph(visited map)/ queue and connect all neigbors
            for neighbor in curr.neighbors:
                if neighbor not in visited_map:
                    visited_map[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited_map[curr].neighbors.append(visited_map[neighbor])
        # Step3 : No scanning phase for BFS            
        # Step 4 : Return result        
        return visited_map[node]


# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V)....create size V Map and size V queue
def test():
    sol = Solution()
    n1 = Node(1)
    result = sol.cloneGraph(n1)
    print(f"Result: {result.val}")
test()


