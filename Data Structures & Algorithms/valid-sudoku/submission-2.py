"""
 OOD: No
 Constraints: No
 input : List[List[str]]
 output : boolean
"""
# Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
# Image : Imagine an instant-lookup Map Traverse an array to check if a Key or Value exists before , then perform following actions
#Tricks: if hashmap's key contains multiple value: use defaultdict(list) - or defaultdict(set) check duplicate
from typing import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board:List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)
       
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                squreKey = (r//3, c//3)
                if board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in square[squreKey]:
                    return False
                row[r].add(board[r][c])
                column[c].add(board[r][c])
                square[squreKey].add(board[r][c])
        # Step 3: 全部跑完沒問題
        return True

# Time complexity: O(9*9) =O(1) ... Traverse size 9*9 Array
# Space complexity:  O(1)....create total size 9*9 HashSet


