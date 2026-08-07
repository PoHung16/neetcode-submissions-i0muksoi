"""
 OOD: No
 Constraints: No
 input : List[List[str]]
 output : boolean
"""
# Optimal Solution:
    # Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
    # Approach : Use a O(1) HashMap Traverse an array to check if a Key or Value exists before , then perform following actions
    # Tricks:
        # if hashmap's key contains multiple value: use defaultdict(list) - or defaultdict(set) check duplicate

from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]])-> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set)
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                sqaureMapKey = (r//3, c//3)
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowMap[r] or board[r][c] in colMap[c] or  board[r][c] in squareMap[sqaureMapKey]:
                    return False
                rowMap[r].add(board[r][c])
                colMap[c].add(board[r][c])
                squareMap[sqaureMapKey].add(board[r][c])
                
        return True



# Time complexity: O(9*9) =O(1) ... Traverse size 9*9 Array
# Space complexity:  O(1)....create total size 9*9 HashSet



def test():
    sol = Solution()
    board =[["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]]

    result = sol.isValidSudoku(board)
    print(f"Result:result")

if __name__ == "__main__":
    test()




