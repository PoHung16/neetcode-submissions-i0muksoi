class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # --- 步驟 1：建立圖與入度表 ---
        # graph: 存儲課程的依賴關係 (鄰接表)
        # in_degree: 記錄每門課還有幾門先修課沒修 (入度)
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        # --- 步驟 2：找起點 (入度為 0 的課) ---
        # 這些是沒有任何先修限制，可以直接修的課
        queue = deque([i for i in range(numCourses) if in_degree[i]==0])
        # --- 步驟 3：開始剝洋蔥 (BFS) ---
        count = 0
        while queue:
            # 彈出一門可以直接修的課
            course = queue.popleft()
            count +=1
            # 檢查所有依賴這門課的後續課程 (neighbors)
            for neighbor in graph[course]:
                # 因為 course 修完了，後續課程的先修限制就少一個
                in_degree[neighbor] -=1
                # 如果 neighbor 的先修課都修完了 (入度變 0)
                # 它就變成了下一波可以修的課
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        # --- 步驟 4：判斷結果 ---
        # 如果修完的數量等於總課程數，代表沒有環
        return count == numCourses


        