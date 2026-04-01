from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Step 1: 初始化三個桶子 (Set 分類)
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # Key 為 (r//3, c//3)

        # Step 2: 遍歷整個 9x9 棋盤
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": # 跳過空格
                    continue
                
                # Step 2-1: 建立 Key (行、列、九宮格的識別碼)
                square_key = (r // 3, c // 3)

                # Step 2-2: 檢查是否在目前的分類中出現過 (Lookup)
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in squares[square_key]):
                    return False
                
                # Step 2-3: 歸類存入
                rows[r].add(val)
                cols[c].add(val)
                squares[square_key].add(val)

        # Step 3: 全部跑完沒問題
        return True