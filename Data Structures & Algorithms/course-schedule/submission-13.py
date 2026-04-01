from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 題型Keyword: “Course Schedule”  or “Graph Valid Tree”
        # 腦中圖像: Detecting Cycles in a Graph- If the course is currently in DFS path and meet VISITING TAG ，就代表有環。
        # 動作記憶法 - 4個步驟 
        # ps.Edge case
        if not prerequisites or numCourses==0:
            return True
        # ps.Decide if its’ a matrix or adjacent list graph -> adjacent list graph
        # Step 1: Build the Graph- directed or undirected graph (Only for Adjacent graph) 
        graph = defaultdict(list)#如果Key不存在，它會自動幫你建立一個空的 list
        for a,b in prerequisites: 
            graph[a].append(b)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        # Step 2: Exploring Phase - dfs : decide if there's a cycle 
        def dfs(i):
            # 2-A Base case
            if states[i]==VISITED: return False # There is no cycle
            if states[i]==VISITING: return True # There is a cycle
            # 2-B Every layer: MARK Twkce & MOVE -  states[i] = VISITING, dfs for neighbor in graph[i] ,  if dfs(neighbor) return True
            states[i] = VISITING
            for neighbor in graph[i]:
                if dfs(neighbor):# 如果鄰居告訴我「有環！」
                    return True
            states[i] = VISITED
            return False
        #Step 3: Scanning Phase -  Perform Dfs on every single element  to find result
        for i in range(numCourses):
            if dfs(i): return False
        #Step 4 : Return result
        return True

# Time complexity: O(V+E) ...visited all nodes and its neighbor
# Space complexity:  O(N)....we have N dfs
def test():
    sol = Solution()
    result = sol.canFinish(2,[[0,1]])
    print(f"Result: {result})")






        