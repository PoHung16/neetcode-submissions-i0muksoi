"""
 OOD: No
 Constraints: No
 input : List[List[int]], List[int]
 output : List[List[int]]
"""
# Optimal Solution
    # Goal : O(N^2) -> O(N)
    # Keyword: "Intervals Problem" -> Linear Scan Intervals (Sort + Linear scan)
        # Edge case
    # Approach:
        # 1. Sort: Order by start time. 
        # 2. Single Loop to traverse the interval:  
            # if conflict : previous end >= current start
            # no conflict : previous end < current start
    # Tricks
        # Insert intertvals is different - while loop
        # 1. Sort: Order by start time. 
        # 2. Single Loop to traverse the interval: its comparing current interval with newInterval
            # no conflict : current interval end < newInterval start  
            # if conflict: 
                # Condition A - current interval end >= newInterval start(automatically fullfill since previous step)
                # Condution B - current interval start <= newInterval end
            # leftover
            
from typing import List
class Solution:
    def insert(self, intervals:List[List[int]],newInterval:List[int]) -> List[List[int]]:
        # 1. Sort: already sorted
        # 2. Single Loop to traverse the interval: its comparing current interval with newInterval
            # no conflict: current interval end < newInterval start  
            # if conflict: 
                # Condition A - current interval end >= newInterval start(automatically fullfill since previous step)
                # Condution B - current interval start <= newInterval end
            # leftover
        n = len(intervals)
        i = 0 
        res = []
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        while i < n and  intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i+=1

        return res
# Time : O(N)...traverse size N array
# Space: O(N)... create size N output list

def test():
    sol = Solution()
    intervals =  [[1,3],[6,9]]
    newInterval = [2,5]
    result = sol.insert(intervals, newInterval)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()
