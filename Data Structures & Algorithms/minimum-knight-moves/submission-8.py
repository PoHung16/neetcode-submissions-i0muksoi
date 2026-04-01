class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # Step 1: Init 3 things
        x, y = abs(x), abs(y)
        queue = deque([(0,0,0)])
        visited = set([(0,0)])
        directions = [
            (2,-1),(2,1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)
        ]
        # step 2:
        while queue:
            cx, cy , moves = queue.popleft()
            if (cx, cy) == (x,y):
                return moves
            for dx,dy in directions:
                nx, ny = cx+dx, cy+dy
                if (nx,ny) not in visited and nx >= -2 and ny >= -2:
                    visited.add((nx,ny))
                    queue.append((nx,ny,moves+1))
        return -1