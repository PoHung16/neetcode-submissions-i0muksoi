from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 題型Keyword:  “shortest path” or “clone graph”
        # 腦中圖像: “Level by level traverse graph ”
        # 動作記憶法 - 三個步驟
        # Step 1: Put original node/ clone node in 
        # visited Map/Set
        # Queue for processing its neighbor
        m, n = len(heights), len(heights[0])
        p_que = deque([])
        a_que = deque([])
        a_visited = set()
        p_visited = set()
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
        # Step2: Process Queue for BFS for P and A (Adjacenet List or grid)
        def bfs(queue,visited):
            while queue:
                #2-A: 拿出original node
                i,j = queue.popleft()
                #2-B: Traverse original node的所有鄰居 -grid
                for i_offset, j_offset in [(1,0),(-1,0),(0,1),(0,-1)]:
                    r ,c = i + i_offset, j + j_offset
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))
        bfs(p_que,p_visited)
        bfs(a_que,a_visited)

        return list(p_visited.intersection(a_visited))

# Time Complexity: O(m*n)...travser m*n grid
# Space Complexity: O(m*n)...create size M*N queue and map












