from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # 題型Keyword:  “shortest path” or “clone graph”
        # 腦中圖像: “Level by level traverse graph ”
        # 動作記憶法 - 三個步驟
        m, n = len(heights), len(heights[0])
        p_que = deque()
        a_que = deque()
        p_visited = set()
        a_visited = set()
        
        # Step 1 :Deal with the original node
        #Put the original node in visited Map/Set
        #Put the original node into the queue for processing its neighbor
        for j in range(n):
            p_que.append((0, j))
            p_visited.add((0, j))
            
        for i in range(1, m):
            p_que.append((i, 0))
            p_visited.add((i, 0))
            
        for i in range(m):
            a_que.append((i, n - 1))
            a_visited.add((i, n - 1))
            
        for j in range(n - 1):
            a_que.append((m - 1, j))
            a_visited.add((m - 1, j))

        # Step2:  Process Queue for BFS
        def get_coords(queue, visited):
            
            while queue:
                i, j = queue.popleft()
                # 2-B-1 Deal with the original neighbor node
                for i_off, j_off in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    r, c = i + i_off, j + j_off
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j] and (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c))
            
        get_coords(p_que, p_visited)
        get_coords(a_que, a_visited)
        return list(p_visited.intersection(a_visited))

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)












