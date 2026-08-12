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
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Brute Force: O(N^2)
    # Keyword: "Intervals Problem" -> Linear Scan Intervals (Sort + Linear scan)
    # Approach:
        # 1. Edge case
        # 2. Sort: Order by start time
        # 3. Linear Scan: Single loop to traverse intervals
            # No conflict: previous end < current start
            # conflict: previous end >= current start
    # Tricks:
        # Meeting Rooms II
        # 1. Edge case
        # 2. Sort: Order by start time
        # 3. Tracking: Use a list to store the end time of each active room.
        # 4. Linear Scan: Single/Nested loop to traverse meeting and room
            # if free room : Reuse the room & update end time.
            # no free room : append a new room
# 暴力解因為不知道哪間房最快空，所以要翻一圈找，才需要 placed 記號注記meeting有沒有被placed；
# Heap 一眼就看到最快退房的那間，代表meeting 一定會被placed,不需要Flag

class Solution:
    def minMeetingRooms(self, intervals:List[Tuple[int]])->int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        rooms = []
        for meeting in intervals:
            placed = False
            for i in range(len(rooms)):
                if rooms[i].end <= meeting.end:
                    rooms[i].end = meeting.end
                    placed = True
                    break
                if not placed:
                    rooms.append(meeting.end)
        return len(rooms) # how many room we need

# Optimal Solution
    # Keyword: "Intervals Problem" -> Linear Scan Intervals (Sort + Linear scan)
    # Keyword: "Return minimum number" -> Greedy 
        # Greedy Sometimes can use  Min-Heap to replace linear scan
        # We don't need to check ALL active rooms; we only care about the EARLIEST available room (min_heap[0]).    
    # Tricks:
        # Meeting Rooms II
        # 1. Edge case
        # 2. Sort:  Tracking: Use a Min-Heap to store the end times of active rooms.
        # 3. Tracking: Use a list to store the end time of each active room.
        # 4. Linear Scan: Single/Nested loop to traverse meeting 
            # if free room : Reuse the room & update end time.
            # no free room : append a new room
    
    
from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        for meeting in intervals:
            if min_heap and min_heap[0] <= meeting.start:
                heapq.heappop(min_heap) # pop old end time
                heapq.heappush(min_heap, meeting.end)# update end time            
            else:
                heapq.heappush(min_heap,meeting.end)
        # 4. 最後 Heap 的大小就是「開過的最多房間數」
        return len(min_heap)   
    
 
# Time Complexity:  O(N log N) 
    #- O(N log N) for sorting 
    #-  N times* heap operations at O(log N) each.
# Space Complexity: O(N)... create size N heap


def test():
    sol = Solution()
    intervals = [Interval(0,40), Interval(5,10), Interval(15,20)]
    result = sol.minMeetingRooms(intervals)
    print(f"Result: {result}")  # 預期輸出: 2


if __name__ == "__main__":
    test()
        








