class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #題型Keyword: "Set Matrix Zeroes"
        #腦中圖像:  「第一列是備忘錄 (Memo on Edge)」 — 為了省空間，我們不拿新筆記本，直接把矩陣的「第一列」和「第一行」當作記號區。
        rowZero = False
        rows = len(matrix)
        cols = len(matrix[0])
        #Step 1 : Scan & Flag：掃描整個矩陣。
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    #如果 (i, j) 是 0且不在第一列，在第一列的 (0, j) 和第一行的 (i, 0) 打個叉（設成 0）。
                    if r > 0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
                    #如果 (i, j) 是 0且在第一列，先用變數記下「第一行/列本身是否原本就有 0」。
                    else:
                        rowZero = True
        # Step 2: Set Zeroes：根據第一行和第一列的「叉叉」，把第一行和第一列內部所有的元素填成 0。
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        #Step 3: Handle Memo & TOP-LEFT corner：最後根據開頭記下的變數，處理第一行和第一列自己的命運
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0
        



        '''
        Time Complexity : O(M*N) -> traverse size M*N 陣列
        Space Complexity: O(1) ...create no variable
        '''
        
        