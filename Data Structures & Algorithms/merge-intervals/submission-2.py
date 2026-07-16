"""
 OOD: No
 Constraints: No
 input : List[List[int]]
 output : List[List[int]]
"""

# Optimal Solution - Brute Force for Insert Interval
    # Keyword: "Intervals Problem" -> Linear Scan Intervals
    # Approach: 
        #  sort the entire list by start times, 
        # and then traverse intervals array to merge overlapping intervals  
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged

# Time complexity: O(N log N) ...  sorting the array of size N
# Space complexity: O(N) ... the size of output list

def test():
    sol = Solution()
    intervals = [[1,3],[1,5],[6,7]]
    result = sol.merge(intervals)
    print(f"result:{result}") # Expected output: [[1,5],[6,7]]
if __name__ == "__main__":
    test()