"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 題型Keyword: “Minimum Operations”
        # 腦中圖像: “公車上下車” -> Start 是上車 (+1 room)，End 是下車 (-1 room)。我們要找的是「這台公車最擠的時候」有多少人。
        # 動作記憶法 - 三個步驟 
        
        # Step 1: Flatten Time tag with +1 或 -1。 and Sort by Time (按時間排序)
        time_points = []
        for i in intervals:
            time_points.append((i.start, 1))   # Arrival: Need a room
            time_points.append((i.end, -1))    # Departure: Free up a room
        # 如果時間相同，讓 -1 (離開) 先發生，這樣 8:00 走、8:00 進就不會衝突。
        time_points.sort(key=lambda x: (x[0], x[1]))

        #(0,1) (40,-1) (5,1) (10,-1)

        # Step 2: Iterate the Time tag array to find the "Peak"
        res = 0
        count = 0
        for t in time_points:
            count += t[1]          # 當下房間需求量的增減
            res = max(res, count)  # 隨時記錄「最高峰」的需求
            
        return res

        '''
        Time Complexity : O(N logN)
            - O(N logN) ... Sort time points
            - O(N) ... Create time points
        Space Complexity : O(N)
            - O(N) ... Store 2N time points
        '''