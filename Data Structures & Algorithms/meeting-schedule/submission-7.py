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
# Brute Force: 
    # Array , Interval Problem
    # Use Nested loop to compare every meeting pair have conflict - max(s1,s2) < min(e1,e2)-> O(N^2)
class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int]]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if max(intervals[i].start,intervals[j].start) < min(intervals[i].end, intervals[j].end):
                    return False
        return True
                
# Optimal Solution
    # Goal : O(N^2) -> O(N)
    # Keyword: "Intervals Problem" -> Linear Scan Intervals
    # Approach:
        # 1. Sort: Order by start time. 
        # 2. Clash: Traverse loop and compare consecutive meeting start time and end time
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        for i in range(1,len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
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


