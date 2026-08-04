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
    # Goal : O(N^2) -> O(N)
    # Keyword: "Intervals Problem" -> Linear Scan Intervals (Sort + Linear scan)
        # Edge case
    # Approach:
        # 1. Sort: Order by start time. 
        # 2. Single Loop to traverse the interval:  
            # if conflict : previous end> current start ,return False
            # no conflict : return True
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int]]) -> bool:
        # edge case
        if not intervals:
            return True
        # 1. Sort: Order by start time. 
        intervals.sort(key=lambda x:x.start)
        # 2.Single Loop to traverse the interval: 
        for i in range(1,len(intervals)):
            # if conflict : previous end> current start
            if intervals[i-1].end > intervals[i].start:
                return False
            
        # no conflict : return True
        return True


# Time complexity: O(N log N) ... Sorting
# Space complexity: O(1)

def test():
    sol = Solution()
    intervals = [Interval(0,30), Interval(5,10), Interval(15,20)]
    result = sol.canAttendMeetings(intervals)
    print(f"result:{result}") 
if __name__ == "__main__":
    test()


