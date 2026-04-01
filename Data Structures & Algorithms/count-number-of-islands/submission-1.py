class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 題型Keyword: “Islands problem”
        # 腦中圖像: 一個人四面走到底探險，遇到牆或走過的路就退後一步，換條路
        # 動作記憶法 - 三個步驟
        m, n = len(grid), len(grid[0])
        num_islands = 0
        
        #Step2. Marking & Exploring Phase - dfs
        def dfs(i, j):
            #2-A Base case: 超出邊界或是遇到水 (grid[i][j] != "1")，就停下
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return
            #2-B: 原地修改，防止之後重複計算 ，並consider 4 diectional dfs
            else:
                grid[i][j] = "0"
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)
        #Step1. Scanning Phase - 用dfs 去把這整塊相連的陸地找出來。
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j)
        #Step 3 : Return result
        return num_islands

# Time Complexity: O(m*n)....traverse m*n grid
# Space Complexity: O(m*n).... m*n個dfs 