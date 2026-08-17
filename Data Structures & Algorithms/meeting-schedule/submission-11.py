"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
 OOD: No
 Constraints: No
 input : List[Tuple[int]]
 output : boolean
"""
# Optimal Solution
    # Keyword: "Intervals Problem" -> Linear Scan Intervals (Sort + Linear scan)
        # Edge case
    # Approach:
        # 1. Edge case
        # 2. Sort: Order by start time
        # 3. Linear Scan: Single loop to traverse intervals
            # No conflict: previous end < current start -> return True
            # conflict: previous end >= current start -> return False
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[Interval])-> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        for i in range(1,len(intervals)):
            if intervals[i-1].end <= intervals[i].start:
                continue
            else:
                return False
        return True

# Time complexity: O(N log N) ... Sorting
# Space complexity: O(1)

def test():
    sol = Solution()
    intervals =  [Interval(0,30), Interval(5,10), Interval(15,20)]
    result = sol.canAttendMeetings(intervals)
    print(f"result:{result}") 
if __name__ == "__main__":
    test()


