class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #題型Keyword “Rotate 90 degrees”
        #腦中圖像: Transpose (對角線對折) 

        # Step 1: Transpose (對角線對折) -對角線上方由i+1開始
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                # 交換對稱位置
                matrix[i][j] ,matrix[j][i] = matrix[j][i], matrix[i][j]
        # Step 2: Reverse Rows (左右翻轉) - 左右pointer對調
        for i in range(n):
            for j in range(n //2):
                matrix[i][j] ,matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

        '''
        Time Complexity: O(N^2)..Nested Loops
        Space Complexity: O(1) ...create no variable
        '''

      
