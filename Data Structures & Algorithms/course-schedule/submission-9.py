from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 題型Keyword: “Course Schedule”  or “Graph Valid Tree”
        # 腦中圖像: Detecting Cycles in a Graph- If the course is currently in DFS path and meet VISITING TAG ，就代表有環。
        # 動作記憶法 - 三個步驟 
        # ps.Edge case
        if not prerequisites or numCourses==0:
            return True
        #Step 1: build up the graph - directed graph/ undirected graph
        graph = defaultdict(list)#如果Key不存在，它會自動幫你建立一個空的 list
        for a,b in prerequisites: 
            graph[a].append(b) #key is going to map to its prerequisites
        #Step 2:  Exploring Phase - dfs : decide if there's a cycle (AdjacentList or matrix)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        def dfs(i):
            # 2-A Base case
            if states[i] == VISITED: return False
            if states[i] == VISITING: return True
            # 2-B Every layer - 將狀態設為 VISITING, 探索鄰居，如果有環 return True, 如果沒環標記為VISITIED return False
            # 開始探索：
            states[i] = VISITING
            for neighbor in graph[i]:
                if dfs(neighbor): return True
            states[i] = VISITED
            return False

        #Step 3: Scanning Phase - use dfs on every single element to find out if there's a cycle in graph
        for i in range(numCourses):
            if dfs(i): return False
        return True






































        
        
        

        

        

# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(N)....we have N dfs


        