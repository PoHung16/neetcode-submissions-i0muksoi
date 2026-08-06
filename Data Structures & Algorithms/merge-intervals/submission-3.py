"""
 OOD: No
 Constraints: No
 input : List[List[int]]
 output : List[List[int]]
"""

# Optimal Solution - Brute Force for Insert Interval
    # Keyword: "Intervals Problem" -> Linear Scan Intervals
    # Approach:
        # 1. Sort: Order by start time. 
        # 2. Single Loop to traverse the interval:  
            # if conflict : previous end >= current start
            # no conflict : previous end < current start
from typing import List
class Solution:
    def merge(self, intervals:List[List[int]])->List[List[int]]:
        if not intervals:
            return []
        # 1. Sort: Order by start time. 
        intervals.sort(key=lambda x:x[0])
        merge = [[intervals[0][0],intervals[0][1]]]
        # 2. Single Loop to traverse the interval:  
            # if conflict : previous end >= current start
            # no conflict : previous end < current start
        for i in range(1,len(intervals)):
            if merge[-1][1] >= intervals[i][0]:
                merge[-1][1] = max(merge[-1][1], intervals[i][1])
            else:
                merge.append(intervals[i])
        return merge

# Time complexity: O(N log N) ...  sorting the array of size N
# Space complexity: O(N) ... create size N output list

def test():
    sol = Solution()
    intervals = [[1,3],[1,5],[6,7]]
    result = sol.merge(intervals)
    print(f"result:{result}") # Expected output: [[1,5],[6,7]]
if __name__ == "__main__":
    test()