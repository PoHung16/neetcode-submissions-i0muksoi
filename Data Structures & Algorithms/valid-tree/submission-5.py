class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 題型Keyword:  “Course Schedule" or "Graph Valid Tree"
        # 腦中圖像: Detecting Cycles in a Graph- If the course is currently in DFS path and meet VISITING TAG ，就代表有環。
        # 動作記憶法 - 三個步驟 
        # ps.Edge case: A tree with n nodes MUST have exactly n-1 edges.
        if len(edges) != n - 1:
            return False
        # Step 1: Build the graph (Adjacency List)
        ## Since it's undirected, we add the connection both ways.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # States: 0 = Unvisited, 1 = Visiting, 2 = Visited
        UNVISITED = 0
        VISITING = 1
        states = [UNVISITED] * n
        visited_set = set() # <--- 這裡建立一個真正的 Set
        # Step 2: Exploring Phase - dfs : decide if there's a cycle
        def dfs(i, parent):
            #2-A Base case
            if states[i] == VISITING: return True
            if i in visited_set: return False # 如果已經在 Set 裡，代表這條路穩了
            #2-B Every layer:
            # 開始探索：將狀態設為 VISITING
            states[i] = VISITING
            # Crucial: Don't go back to the node you just came from!
            for neighbor in graph[i]:
                # Crucial: Don't go back to the node you just came from!
                if neighbor == parent:
                    continue
                if dfs(neighbor, i):
                    return True
            # 探索完成：所有鄰居都檢查過了，沒發現環，標記為已存取
            visited_set.add(i)
            return False
        # Step 3: Start the scan from the first node (0)
        # If there's a cycle, it's not a tree.
        if dfs(0, -1):
            return False
        return len(visited_set) ==n


# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V+E)....we have V+E dfs













