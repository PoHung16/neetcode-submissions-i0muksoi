"""
 OOD: No
 Constraints: No
 input : List[Tuple[int]]
 output : boolean
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Brute Force: 
    # For each meeting, loop through all currently active rooms. If a room becomes free,
    # assign the meeting to it. If no rooms are free, create a new room -> O(N^2)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by start time first
        intervals.sort(key=lambda x: x[0])
        rooms = [] # stores the end times of meetings in each room
        
        for meeting in intervals:
            placed = False
            for i in range(len(rooms)):
                # If the room is free (end time <= current start)
                if rooms[i] <= meeting[0]:
                    rooms[i] = meeting[1] # update end time
                    placed = True
                    break
            if not placed:
                rooms.append(meeting[1]) # open a new room
                
        return len(rooms)

import heapq
from typing import List


# Optimal Solution
    # Keyword: "Room allocation" -> Min-Heap
    # Approach: 
        # 1. Sort: Order by start time (process chronologically).
        # 2. Heap: Track the earliest free room (min-heap stores end times).
        # 3. Reuse: If current start >= heap top -> Pop old room (reuse), then push new end.
        #           Otherwise -> Just push new end (open new room).
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        # 1. Sort by start time
        # Access attributes .start and .end instead of using index [0] and [1]
        intervals.sort(key=lambda x: x.start)
        
        # 2. Initialize min-heap with the end time of the first meeting
        not_free_rooms = []
        heapq.heappush(not_free_rooms, intervals[0].end)
        
        # 3. Process remaining meetings
        for meeting in intervals[1:]:
            current_start = meeting.start
            current_end = meeting.end
            
            # If the room that finishes earliest is free, we reuse it!
            # (Note: (0,8),(8,10) is NOT a conflict, so '<=' works perfectly)
            if not_free_rooms[0] <= current_start:
                heapq.heappop(not_free_rooms)
                
            # Always push the current meeting's end time into the heap
            heapq.heappush(not_free_rooms, current_end)
            
        # 4. The size of the heap is the minimum rooms required
        return len(not_free_rooms)



#=========================================================================
# When to use standard Greedy:
#   - When we only need to track a SINGLE state (one room, one timeline).
#   - We only need one variable (e.g., prev_end) to confidently sweep forward.
# 
# When standard Greedy is NOT enough:
#   - When we must track MULTIPLE states simultaneously (multiple parallel rooms).
#   - A single variable cannot store all end times, so we need a Min-Heap 
#     to instantly tell us which room becomes free the earliest.
# =========================================================================