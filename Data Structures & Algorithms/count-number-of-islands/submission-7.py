class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 題型Keyword: “Islands problem”
        # 腦中圖像: 一個人四面走到底探險，遇到牆或走過的路就退後一步，換條路
        # 動作記憶法 - 三個步驟
        #ps. edge case
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0

        #Step1. Exploring Phase - dfs
        def dfs(i,j):
            # 2-A Base case: 超出邊界或是遇到水 (grid[i][j] != "1")，就停下
            if i < 0 or i >= m or j< 0 or j>= n or grid[i][j]!= "1":
                return
            # 2-B Every Layer：consider 4 directional dfs - Mark & Move
            grid[i][j] = "0"
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)
        # Step2. Scanning Phase - use dfs on every single element to find out the connected island
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
      
        #Step 3 : Return result
        return count

# Time Complexity: O(m*n)....traverse m*n grid
# Space Complexity: O(m*n).... m*n個dfs 