from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 題型Keyword:  “shortest path” or “clone graph” -> BFS graph
        # 腦中圖像: “Level by level traverse graph ”
        # 動作記憶法 - 4個步驟
        #ps. Edge case:
        if not heights:
            return[]
        #ps.Decide if its’ a matrix or adjacent list graph - > matrix
        # Step 1: Build up the graph 
        # Visited Map/Set: with original node /  clone node
        # Queue for processing its neighbor
        m, n = len(heights), len(heights[0])
        p_que = deque([])
        a_que = deque([])
        p_visited = set()
        a_visited = set()
        for j in range(n):
            p_que.append((0,j))
            p_visited.add((0,j))
        for i in range(1,m):
            p_que.append((i,0))
            p_visited.add((i,0))
        for i in range(m):
            a_que.append((i,n-1))
            a_visited.add((i,n-1))
        for j in range(n-1):
            a_que.append((m-1,j))
            a_visited.add((m-1,j))
        # Step2: Exploring Phase: Process Queue for BFS for P and A - matrix version
        def bfs(visited,queue):
            while queue:
                # 2-A: Take out the queue coordinate one by one
                i,j = queue.popleft()
                # 2-B: Traverse all current node’s neighbor with offset and add to the graph(visited map)/ queue within the condition and border and not in the map
                for i_offset, j_offset in [[1,0],[-1,0],[0,1],[0,-1]]:
                    r, c = i+i_offset, j+ j_offset
                    if 0<=r<m and 0 <=c<n and heights[r][c] >= heights[i][j] and (r,c) not in visited:
                        visited.add((r,c))
                        queue.append((r,c))
        bfs(p_visited,p_que)
        bfs(a_visited,a_que)
        # Step3 : No scanning phase for BFS            
        # Step 4 : Return result : visited set -> list
        return list(p_visited.intersection(a_visited))
                    
                



# Time Complexity: O(m*n)...travser m*n grid
# Space Complexity: O(m*n)...create total size M*N queue and visited set












