class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 題型Keyword: “Islands problem” or “connected component” -> DFS Graph
        # 腦中圖像:There’s a person try to explore every path, once he hits the wall or visited place. He will choose another path
        # 動作記憶法 - 4個步驟 
        #ps.Edge case
        if n == 0: 
            return 0
        #ps.Decide if its’ a matrix or adjacent list graph -> adjacent graph
        # Step 1: Build the Graph- directed or undirected graph (Only for Adjacent graph) 
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        count = 0
        #Step 2: Exploring Phase - dfs (Adjacent graph Version) 
        def dfs(i):
            #2-a base case: no base case
            #2-b Every Layer： MARK & MOVE for neighbor in graph[i] if neighbor not in visited 
            visited.add(i)
            for neighbor in graph[i]:
                if neighbor not in visited:
                    dfs(neighbor)
        #Step 3: Scanning Phase - Perform Dfs on every single element  to find result
        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i)
        #Step 4 : Return result
        return count


# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(V+E).... we have V 個dfs  but create size V+E graph since its undirected

def test():
    sol = Solution()
    result = sol.countComponents(5,[[0,1],[1,2],[3,4]])
    print(f"Result: {result}")

test()
        
       

        

    










        