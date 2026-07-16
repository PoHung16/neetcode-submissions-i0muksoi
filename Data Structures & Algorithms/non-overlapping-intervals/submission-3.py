"""
 OOD: No
 Constraints: No
 input : List[List[int]]
 output : int
"""

# Optimal Solution
    # Keyword: "Minimum removal" -> Greedy (Earliest End Time)
    # Greedy: we just grab whatever looks best at each step, hoping it all works out perfectly in the end.
    # Goal: In this problem, our goal is to "remove the minimum number of intervals." In other words, we want to "keep as many non-overlapping intervals as possible."
    # Approach: 
        # 1. Sort: Order by end time (finish earliest). and then we can have more intervals to stay
        # 2. Clash: If it starts too early (ealier than previous end) -> Delete it.
        
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) ->int:
        # 1. Sort by end time
        intervals.sort(key=lambda x: x[1])
        removed_count = 0
        prev_end = intervals[0][1]

        # 2. Clash
        for i in range(1, len(intervals)):
            current_start = intervals[i][0] 
            current_end = intervals[i][1]
            # overlap!
            if current_start < prev_end:
                removed_count+=1
            # No overlap, update the prev_end to current interval's end
            else:
                prev_end = current_end

        return removed_count
# Time complexity: O(N log N) ... Due to sorting the intervals
# Space complexity: O(N) ... in Python, it silently consumes O(N) auxiliary space when you call sort()

def test():
    sol = Solution()
    intervals = [[1,2],[2,4],[1,4]]
    result = sol.eraseOverlapIntervals(intervals)
    print(f"result:{result}") # Expected output: 1 (remove [1,4])
if __name__ == "__main__":
    test()