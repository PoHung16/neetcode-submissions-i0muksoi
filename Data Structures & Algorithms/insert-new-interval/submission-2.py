"""
 OOD: No
 Constraints: No
 input : List[List[int]], List[int]
 output : List[List[int]]
"""
# Brute Force: 
    # Insert the new interval into the list, sort the entire list by start times, 
    # and then traverse intervals array to merge overlapping intervals  -> O(N log N)
from typing import List
class Solution:
    def insert(self, intervals:List[List[int]], newInterval:List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1],interval[1])
        return merged

# Optimal Solution
    # Keyword: "Intervals Problem" -> Linear Scan Intervals
    # Approach: Since the input is already sorted, we can build the result from O(NlogN) -> O(N)
        # 1. Left: Add everything before the new interval.
        # 2. Middle: Merge everything that overlaps.
        # 3. Right: Add everything after the new interval.
    
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # 1. Left: Add everything before the new interval.
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # 2. Middle: Merge everything that overlaps.
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i+=1
            res.append(newInterval)

        # 3. Right: Add everything after the new interval.
        while i < n:
            res.append(intervals[i])
            i+=1
        return res

        
# Time complexity: O(N) ... Traverse size N Array
# Space complexity: O(N) ... the size of output list

def test():
    sol = Solution()
    intervals =  [[1,3],[6,9]]
    newInterval = [2,5]
    result = sol.insert(intervals, newInterval)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()











class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #題型Keyword: “Merge”, “Insert”
        #腦中圖像:  “貪吃蛇“ -> 後面的頭如果撞到前面的尾，就把前面的尾巴拉長。
        #動作記憶法 - 三個步驟 
        # Step 1: Sort: 先按起點排序 (Start time)。 This is already sorted
        # Step 2:  Iterate to build res
        res = []
        i = 0
        # Add left part (no overlap)
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i +=1
        # Merge Overlapping and insert newInterval part: IS <= NE
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max (intervals[i][1],newInterval[1])
            i+=1
        res.append(newInterval)
        #Add Right part : IS> NE
        while i < len(intervals):
            res.append(intervals[i])
            i+=1
        return res
        '''
        Time Complexity : O (N)
            - O(N)... Traverse size N Array
        Space Complexity - O(N)
            - O(N) ….Create Size N List
        '''
    
       
    
        




    
    
    