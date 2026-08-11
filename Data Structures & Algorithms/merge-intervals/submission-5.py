"""
 OOD: No
 Constraints: No
 input : List[List[int]]
 output : List[List[int]]
"""

# Optimal Solution - Brute Force for Insert Interval
    # Keyword: "Intervals Problem" -> Linear Scan Intervals
    # Approach:
        # 1. Edge case
        # 2. Sort: Order by start time
        # 3. Linear Scan: Single loop to traverse intervals
            # No conflict: previous end < current start
            # conflict: previous end >= current start
from typing import List
class Solution:
    def merge(self, intervals:List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        mergeInterval = []
        mergeInterval.append(intervals[0])
        for i in range(1,len(intervals)):
            if mergeInterval[-1][1] < intervals[i][0]:
                mergeInterval.append(intervals[i])
            else:
                mergeInterval[-1][0] = min(mergeInterval[-1][0],intervals[i][0])
                mergeInterval[-1][1] = max(mergeInterval[-1][1],intervals[i][1])
        return mergeInterval

# Time complexity: O(N log N) ...  sorting the array of size N
# Space complexity: O(N) ... create size N output list

def test():
    sol = Solution()
    intervals = [[1,3],[1,5],[6,7]]
    result = sol.merge(intervals)
    print(f"result:{result}") # Expected output: [[1,5],[6,7]]
if __name__ == "__main__":
    test()