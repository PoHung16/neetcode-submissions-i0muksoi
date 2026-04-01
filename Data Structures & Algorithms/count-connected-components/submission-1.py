class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #題型Keyword: “connected components”
        #腦中圖像:
        #動作記憶法 - 三個步驟 
        # Step1: Build the graph - undirected graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        visited = set()
        count = 0
        #Step 2:  Exploring Phase - dfs
        def dfs(node):
            #2-a Base case: 
            #2-b Every Layer
            visited.add(node)
            for neighbor in graph[node]: # 同步更換
                if neighbor not in visited:
                    dfs(neighbor)

        #Step 3: Scanning Phase - use dfs on every single element to find out the connected island
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        #Step 4 : Return result
        return count

    

# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V+E).... create size V+E graph since its undirected, we have V 個dfs 








        