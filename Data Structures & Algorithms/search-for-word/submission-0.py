"""
 OOD: No
 Constraints: n <= 20
 input : List[List[str]], str
 output : boolean
"""
# Optimal Solution
    # Keyword : "Word Search"  -> Grid DFS Backtracking
    # Approach:  Define a DFS function to find the next character, keep track of length. If an element hasn't been used yet, pick it, mark it as used, and move to the next position.
    # Tricks
        # Tricks - DFS
            # 1.Draw a decision tree to help us understand recursive problem
            # 2.Procedure: base case -> current level -> next level
        # Tricks - Grid DFS
            # 1. Base case 1: if index k == len(word), we found the whole word -> return True.
            # 2. Base case 2: out of bounds or mismatch char -> return False.
            # 3. Mark visited: track path by changing board[r][c] = '#' to save space, restore it during backtrack.
            # 4. Short-circuit: use 'or' to connect 4 directions. If any direction hits True, stop exploring immediately.

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str)-> bool:
        rows, cols = len(board), len(board[0])
        def dfs(r,c,k):
            # base case 1: found the entire word successfully!
            if k == len(word):
                return True
            # base case 2: out of bounds, or character doesn't match
            if r < 0 or c < 0 or r>= rows or c >= cols or board[r][c] != word[k]:
                return False
                
            # current level - pick (In-place marking to save space)
            temp = board[r][c]
            board[r][c] = "#"

            # next level - explore 4 directions (down, up, right, left) using short-circuit 'or'
            res = (dfs(r + 1, c, k + 1) or
                   dfs(r - 1, c, k + 1) or  
                   dfs(r, c + 1, k + 1) or  
                   dfs(r, c - 1, k + 1))    
                   
            # current level - don't pick (Backtrack & restore the original character) -> no next level below
            board[r][c] = temp
            
            return res
        # Try every single cell as potential starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

# Time complexity: O(M * N * 3^L)
  # Traverse M * N  board size to look for the starting character. 
  # At the first cell, we have 4 choices, but for all subsequent cells, we only have up to 3 choices (since we can't go back to the cell we just came from). 
  # The maximum depth of the decision tree is L (length of the word).
# Space Complexity: O(L) ... the maximum depth of the recursion tree is length of the world

def test():
    sol = Solution()
    board = [
      ["A","B","C","D"],
      ["S","A","A","T"],
      ["A","C","A","E"]
    ]
    word = "CAT"
    result = sol.exist(board, word)
    print(f"Result: {result}")  # Expected: True

if __name__ == "__main__":
    test()
