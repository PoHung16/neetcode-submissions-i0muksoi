class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 題型Keyword: “Course Schedule”  or “Graph Valid Tree”
        # 腦中圖像: Detecting Cycles in a Graph- If the node is currently in DFS path and meet VISITING TAG ，就代表有環。
        # 動作記憶法 - 三個步驟 
        # ps.Edge case: A tree with n nodes MUST have exactly n-1 edges.
        if len(edges) != n-1:
            return False
        # Step1: Build the graph - undirected grapg
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        #Step 2:  Exploring Phase - dfs : detect if there's a cycle
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * n
        def dfs(i,parent):
            # 2-A Base case
            if states[i] == VISITED: return False
            if states[i] == VISITING: return True
            # 2-B Every layer - 將狀態設為 VISITING, 探索鄰居，如果有環 return True, 如果沒環標記為VISITIED return False
            states[i] = VISITING
            for neighbor in graph[i]:
                if neighbor == parent: continue
                if dfs(neighbor,i): return True
            states[i] = VISITED
            return False

        #Step 3: Scanning Phase - use dfs on every single element to find out if there's a cycle in graph
        if dfs(0, -1):
            return False

        #在判斷是否為「樹」時，除了不能有環，還有一個條件是：所有節點都必須連在一起。
        for s in states:
            if s!= VISITED:
                return False
        return True
       


# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V)....we have V dfs













