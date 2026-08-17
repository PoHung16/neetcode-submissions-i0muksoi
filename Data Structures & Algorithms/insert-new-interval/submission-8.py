"""
 OOD: No
 Constraints: No
 Input : List[List[int]]
 Output: List[List[int]]
"""
# Optimal Solution
# Keyword: "Intervals Problem" -> Linear Scan Intervals (Sort + Linear scan)
# Approach:
    # 1. Edge case
    # 2. Sort: Order by start time
    # 3. Linear Scan: Single loop to traverse intervals
        # No conflict: previous end < current start
        # conflict: previous end >= current start
# Tricks:
    # Insert intertvals is different - while loop
    # 1. Edge case
    # 2. Sort: Order by start time
    # 3. Linear Scan: while loop to traverse intervals (compare every interval with new interval)
        # No conflict: previous end < current start
        # conflict -因為no sort- newInterval cannot sort, 所以有2情況: 
            # Condition A: previous end >= newInterval start (it must be correct, so we skip it) 
            # Condition B: previous start <= newInterval end (ex:[6,9], newInterval[4,8]) ([10,12], [4,8] -> this wont work)
        # leftover

from typing import List
class Solution:
    def insert(self, intervals:List[List[int]],newInterval:List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        i = 0 
        n = len(intervals)
        res = []
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
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
