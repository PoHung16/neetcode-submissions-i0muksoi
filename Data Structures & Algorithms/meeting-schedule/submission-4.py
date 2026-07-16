"""
 OOD: No
 Constraints: No
 input : List[Tuple[int]]
 output : boolean
"""
# Brute Force: 
    # Compare every meeting with every other meeting using a nested loop.
    # If any two meetings overlap, return False -> O(N^2)
class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int]]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                # Check conflict: max(start1, start2) < min(end1, end2)
                if max(intervals[i].start, intervals[j].start) < min(intervals[i].end, intervals[j].end):
                    return False
        return True


# Optimal Solution
    # Keyword: "Intervals Problem" -> Linear Scan Intervals
    # Approach: 
        # 1. Sort: Order by start time. 
        # 2. Clash: Loop through and compare each meeting's start time with the previous meeting's end time.
from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int]]) -> bool:
        if not intervals:
            return True
            
        # 1. Sort by start time 
        intervals.sort(key=lambda x: x.start)
        # 2. Clash check with the neighbor
        for i in range(1,len(intervals)):
            # If current meeting starts before the previous one ends -> Conflict!
            if intervals[i].start < intervals[i-1].end:
                return False
        return True



# Time complexity: O(N log N) ... Due to sorting the intervals
# Space complexity: O(N) ... Timsort auxiliary space in Python

def test():
    sol = Solution()
    intervals = [Interval(0,30), Interval(5,10), Interval(15,20)]
    result = sol.canAttendMeetings(intervals)
    print(f"result:{result}") # Expected output: False
if __name__ == "__main__":
    test()