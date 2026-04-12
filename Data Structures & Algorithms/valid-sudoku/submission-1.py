from collections import defaultdict
from typing import List
class Solution:
    # Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
    # Image: Imagine an instant-lookup Map where you check if a Key or Value exists before , then perform following actions
    # Workflow - 3 Steps:
    # Step 1: Initialize a map, store the key-value pair
    # Step 2: Traverse the Array to check if a Key or Value exists before,, then perform following actions
    # Step 3: Return the result
    # Tricks:
        # if hashmap's key contains multiple value: use defaultdict(list) - counter array, defaultdict(set) check duplicate
        # if this is a 2D Array:  square_key = (r // 3, c // 3)
    def isValidSudoku(self, board:List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        columnMap = defaultdict(set)
        squareMap = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": # 跳過空格
                    continue
                squreKey = (r//3, c//3)
                if val in rowMap[r] or val in columnMap[c] or val in squareMap[squreKey]:
                    return False
                rowMap[r].add(val)
                columnMap[c].add(val)
                squareMap[squreKey].add(val)
        # Step 3: 全部跑完沒問題
        return True

# Time complexity: O(9*9) =O(1) ... Traverse size 9*9 Array
# Space complexity:  O(1)....create total size 9*9 HashSet


