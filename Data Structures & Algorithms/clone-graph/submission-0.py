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

        #Step1: 把起點放入visited Map並clone起點
        visited = {
            node : Node(node.val)
        }
        # Step2: Process Queue 
        queue = deque([node])
        while queue:
            # 2-A拿出original node
            curr = queue.popleft()
            # 2-B Traverse original node的所有鄰居
            for neighbor in curr.neighbors:
                # 2-B-1: 沒見過的鄰居就放入visited amp並clone , 然後把original neighbor丟進 Queue 準備處理它的鄰居
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # 2-B-2 Connect: 把「clone節點的鄰居」接在「clone節點」後面
                visited[curr].neighbors.append(visited[neighbor])
        #Step 3 : Return result        
        return visited[node]


# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V)....create size V Map and size V queue



