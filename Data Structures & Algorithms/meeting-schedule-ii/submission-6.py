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
# Brute Force: O(N^2)
    # Keyword: "Intervals Problem" -> Linear Scan Intervals (Sort + Linear scan)
        # Edge case
    # Approach
        # 1. Sort: Sort meetings by start time.
        # 2. Tracking: Use a list to store the end time of each active room.
        # 3. Single/Nested Loop to traverse the interval + room:
            # if free room : Reuse the room & update end time.
            # no free room : append a new room
# 暴力解因為不知道哪間房最快空，所以要翻一圈找，才需要 placed 記號注記meeting有沒有被placed；
# Heap 一眼就看到最快退房的那間，代表meeting 一定會被placed,不需要Flag
class Solution:
    def minMeetingRooms(self, intervals:List[Tuple[int]])->int:
        # Edge case
        if not intervals:
            return 0
        # 1. Sort : Sort by start time
        intervals.sort(key=lambda x:x.start)
        # 2. Tracking: Use a list to store the end time of each active room.
        rooms = []
        # 3.  Single/Nested Loop to traverse the interval + room:
        for meeting in intervals:
            placed = False # Flag: Has this meeting been placed into a room?
            for i in range(len(rooms)):
                # if free room : Reuse the room & update end time.
                if rooms[i] <= meeting.start:
                    rooms[i] = meeting.end
                    placed = True
                    break
            # no free room : append a new room
            if not placed:
                rooms.append(meeting.end)
        return len(rooms) # how many room we need

# Optimal Solution
    # Goal: O(N^2)-> O(N)
    # Keyword: "Intervals Problem" -> Linear Scan Intervals (Sort + Linear scan)
        # Edge case
    # Keyword: "Room allocation" -> Min-Heap to replace linear scan
        # We don't need to check ALL active rooms; we only care about the EARLIEST available room (min_heap[0]).
    # Approach
        # 1. Sort: Sort meetings by start time.
        # 2. Tracking: Use a Min-Heap to store the end times of active rooms.
        # 3. Single Loop to traverse the interval:
            # if free room : Reuse the room & update end time.
            # no free room : append a new room
    
from typing import List
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int]]) -> int:
        if not intervals:
            return 0
        # 1. Sort : Sort by start time
        intervals.sort(key=lambda x:x.start) 
        # 2. Rooms: Use a Min-Heap to store the end times of active rooms.
        min_heap = []
        # 3. Single Loop to Check room's for EARLIEST available room 
        for meeting in intervals:
            # If room is free, Reuse room & update end time
            if min_heap and min_heap[0] <= meeting.start:
                heapq.heappop(min_heap) # pop old end time
                heapq.heappush(min_heap, meeting.end) # update end time
            # no free room : append a new room
            else:
                heapq.heappush(min_heap, meeting.end) # update end time       
        # 4. 最後 Heap 的大小就是「開過的最多房間數」
        return len(min_heap)   
    
 
# Time Complexity:  O(N log N) 
    #- O(N log N) for sorting 
    #-  N times* heap operations at O(log N) each.
# Space Complexity: O(N)... create size N heap




        








