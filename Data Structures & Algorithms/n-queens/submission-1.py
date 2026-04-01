class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #Step 1: initialize the final result to store our subsets
        res = []
        board = [["."] * n for i in range(n)]
        #Step 2: define dfs function : def dfs(i)
        def backtrack(r):
            #Step2-1: Base case : when to stop and what should we do
            #既然我們是從第 0 列開始放，當 r 增加到 n 時，代表第 0 到 n−1 列都已經成功放好皇后了。
            '''
            board = [
                [".", "Q", ".", "."],
                [".", ".", ".", "Q"],
                ["Q", ".", ".", "."],
                [".", ".", "Q", "."]
            ]
            這是一個 List of Lists（列表裡面裝列表）。但 LeetCode 要求輸出的每一組答案必須是 List of Strings（列表裡面裝字串），長這樣：
            [" .Q.. ", " ...Q ", " Q... ", " ..Q. "]
            '''
            if r == n:
                copy = ["".join(r) for r in board]
                res.append(copy)
                return
            #Step2-2: Decision Tree Start : include next row
            for c in range(n): #在當前的第 r 列，我們放每一行的位置
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1) 
                    board[r][c] = "." #記得如果Q擺錯了，要回去變成原本的樣子

        #Step 3: call dfs function and return result
        backtrack(0)
        return res

    def isSafe(self, r: int, c: int, board):
        #1. 檢查正上方 (Vertical Check)
        #邏輯：保持列 c 不變，列 row 不斷往上減。
        #白話：看看同一行的上面有沒有皇後。
        row = r - 1 #是為了**「避開自己」
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        #2. 檢查左上對角線 (Diagonal Up-Left)
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        #3. 檢查右上對角線 (Diagonal Up-Right)
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True