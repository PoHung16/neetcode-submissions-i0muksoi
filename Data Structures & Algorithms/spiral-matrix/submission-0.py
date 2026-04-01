class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #題型Keyword:  “Spiral Order”
        #腦中圖像: 想像你在走迷宮，每走完一條邊，那面牆就會向內推一格，活動空間越來越小
        #Step 1: Set Boundaries (架設四面牆) 和方向標 和startpoint
        m, n = len(matrix) , len(matrix[0])
        i, j = 0,0
        res = []
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        direction = RIGHT
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1
        UP_WALL = 0

        #Step 2: Move & Shrink：按照「右 → 下 → 左 → 上」的順序走：
        while len(res) != m*n :
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])#邊move邊append
                    j+=1
                i,j =i+1, j-1 #走到之後i,j改方向
                RIGHT_WALL -=1#Shrink牆壁
                direction = DOWN
            elif direction == DOWN:
                while i < DOWN_WALL:
                    res.append(matrix[i][j])#邊move邊append
                    i+=1
                i,j =i-1, j-1 #走到之後i,j改方向
                DOWN_WALL -= 1#Shrink牆壁
                direction = LEFT
            elif direction == LEFT:
                while j > LEFT_WALL:
                    res.append(matrix[i][j])#邊move邊append
                    j-=1
                i,j =i-1, j+1 #走到之後i,j改方向
                LEFT_WALL += 1#Shrink牆壁
                direction = UP
            elif direction == UP:
                while i > UP_WALL:
                    res.append(matrix[i][j])#邊move邊append
                    i-=1
                i,j =i+1, j+1 #走到之後i,j改方向
                UP_WALL += 1#Shrink牆壁
                direction = RIGHT

        return res
        '''
        Time Complexity: O(M*N)... traverse size M*N 陣列
        Space Complexity: O(M*N) -> 只創了m*n變數 res
        '''


