class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Step 1: 初始化L=0,R = (m * n) - 1「把矩陣拉成一條長線，頭尾開搜。」
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m*n -1
        # Step 2: 循環 while L <= R「手沒交叉就不停」
        while l <= r:
            # Step 2.5: 核心變形 - 座標轉換 
            # row = M // n, 想像你每走 n 格，就會換到下一列。
            # col = M % n, 餘數代表你在換排之後，「剩下」多出來的步數。 
            mid = (l+r) //2
            row = mid // n
            col = mid % n
            mid_val = matrix[row][col]
            # Step 3: 移動mid +/- 1「mid 沒用了，滾吧」
            if mid_val == target:
                return True
            if mid_val < target:
                l = mid + 1
            else:
                r = mid -1
        # Step 4:回傳結果
        return False


            


        