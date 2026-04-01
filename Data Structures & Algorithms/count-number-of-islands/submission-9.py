class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 題型Keyword: “Islands problem” or “connected component”
        # 腦中圖像: 一個人四面走到底探險，遇到牆或走過的路就退後一步，換條路
        # 動作記憶法 - 4個步驟
        #ps.Edge case
        #ps.Decide if its’ a matrix or adjacent graph -> matrix
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        #Step 1: Build the Graph (Only for Adjacent graph)
        #Step 2. Exploring Phase - dfs (Matrix graph Version)
        def dfs(i,j):
            #2-a Base case: 超出邊界或是遇到水 (grid[i][j] != "1")，就停下
            if i < 0 or i >= m or j<0 or j>=n or grid[i][j] != "1" :
                return
            #2-b Every Layer：consider 4 directional dfs - Mark & Move
            grid[i][j] = "0"
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
        
        #Step3 :Scanning Phase : Perform Dfs on every single element  to find result
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        #Step 4 : Return resultt
        return count

# Time Complexity: O(m*n)....traverse m*n grid
# Space Complexity: O(m*n).... m*n個dfs 