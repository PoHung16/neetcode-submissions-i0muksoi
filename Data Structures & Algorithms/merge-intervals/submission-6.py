"""
 OOD: No
 Constraints: No
 input : List[List[int]]
 output : List[List[int]]
"""
# Optimal Solution 
    # Keyword: "Intervals Problem" ->  Linear Scan Intervals (Sort + Linear scan)
    # Approach:
        # 1. Edge case
        # 2. Sort: Order by start time
        # 3. Linear Scan: Single loop to traverse intervals
            # No conflict: previous end < current start , append to final result
            # conflict: previous end >= current start, merge the interval
from typing import List
class Solution:
    def merge(self, intervals:List[List[int]])-> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        res = []
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][0] = min(res[-1][0],intervals[i][0])
                res[-1][1]= max(res[-1][1],intervals[i][1])
        return res

# Time complexity: O(N log N) ...  sorting the array of size N
# Space complexity: O(N) ... create size N output list

def test():
    sol = Solution()
    intervals = [[1,3],[1,5],[6,7]]
    result = sol.merge(intervals)
    print(f"result:{result}") # Expected output: [[1,5],[6,7]]
if __name__ == "__main__":
    test()