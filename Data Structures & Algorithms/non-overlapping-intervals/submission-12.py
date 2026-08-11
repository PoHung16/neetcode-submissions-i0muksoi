"""
 OOD: No
 Constraints: No
 input : List[List[int]]
 output : int
"""
# Optimal Solution
    # Keyword: "Intervals Problem" ->  Linear Scan Intervals (Sort + Linear scan)
    # Keyword: “Return the Minimum number" -> Greedy Choice, we choice intervals that end ealier first to allow more interval coming , then we get the mininum number we need to remove
    # Approach:
    # 1. Edge case
    # 2. Sort: Order by end time (x[1])
    # 3. Linear Scan: Single loop to traverse intervals
        # No conflict: previous end < current start, update previous end
        # conflict: previous end >= current start ,removed_count+=1
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]])->int:
        if not intervals:
            return 0 
        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]
        removed_count = 0
        for i in range(1,len(intervals)):
            if prev_end <= intervals[i][0]:
                prev_end = intervals[i][1]
            else:
                removed_count+=1
        return removed_count

    

# Time Complexity: O(N log N) 
    #- O(N log N) for sorting intervals by end time
    #- O(N) for single loop linear scan
    #- Total: O(N log N)
# Space Complexity: O(1)  

def test():
    sol = Solution()
    intervals = [[1,2],[2,4],[1,4]]
    result = sol.eraseOverlapIntervals(intervals)
    print(f"Result:{result}") # Expected output: 1 (remove [1,4])
if __name__ == "__main__":
    test()