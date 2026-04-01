class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 題型Keyword: “Course Schedule”  or “Graph Valid Tree”
        # 腦中圖像: Detecting Cycles in a Graph- If the node is currently in DFS path and meet VISITING TAG ，就代表有環。
        # 動作記憶法 - 4個步驟 
        #ps.Edge case : A tree with n nodes MUST have exactly n-1 edges.
        #ps.Decide if its’ a matrix or adjacent list graph ->adjacent list graph
        if len(edges) != n-1:
            return False
        #Step 1: Build the Graph- directed or undirected graph (Only for Adjacent graph) 
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        #Step 2: Exploring Phase - dfs : decide if there's a cycle (Adjacent List  graph Version)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * n

        def dfs(i,parent):
            # 2-A Base case
            if states[i] == VISITED: return False
            if states[i] == VISITING: return True
            # 2-B Every layer - MARK Twkce & MOVE - for neighbor in graph[i] , if dfs(neighbor): return True
            states[i] = VISITING
            for neighbor in graph[i]:
                if neighbor == parent: continue
                if dfs(neighbor,i): return True
            states[i] = VISITED
            return False

        #Step 3: Scanning Phase - erform Dfs on every single element  to find result
        if dfs(0, -1):
            return False

        #Step 4 : Return result
        #在判斷是否為「樹」時，除了不能有環，還有一個條件是：所有節點都必須連在一起。
        for s in states:
            if s!= VISITED:
                return False
        return True
       


# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V+E).... create size V+E graph since its undirected, we have V 個dfs 














