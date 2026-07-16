import heapq
from typing import List

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