from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 題型Keyword:  “Course Schedule" - directied grapg
        # 腦中圖像: Detecting Cycles in a Graph- If the course is currently in DFS path and meet VISITING TAG ，就代表有環。
        # 動作記憶法 - 三個步驟 
        # ps.Edge case
        if not prerequisites or numCourses==0:
            return True
        #Step 1: build up the graph
        graph = defaultdict(list) #如果Key不存在，它會自動幫你建立一個空的 list
        courses = prerequisites
        for a,b in courses:
            graph[a].append(b) #key is going to map to its prerequisites

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        #Step 2:  Exploring Phase - dfs : decide if there's a cycle
        def dfs(i):
            #2-A Base case
            if states[i] == VISITED: return False
            if states[i] == VISITING: return True
            #2-B Every layer:
            # 開始探索：將狀態設為 VISITING
            states[i] = VISITING
            for neighbor in graph[i]:
                if dfs(neighbor): 
                    return True #有環
            # 探索完成：所有鄰居都檢查過了，沒發現環，標記為已存取
            states[i] = VISITED
            return False
            
        #Step 3: Scanning Phase - use dfs on every single element to find out if there's cycle in graph
        for i in range(numCourses):
            if states[i] == UNVISITED: # Only start DFS if we haven't been here
                if dfs(i): #有環
                    return False
        return True

# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(N)....we have N dfs


        