"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 題型Keyword:  “判斷/移除 Interval conflicts”
        # 腦中圖像:  “單行道“ ->如果一個車尾還沒開走，下一台車頭就衝進來，就會發生撞車 。
        # 動作記憶法 - 三個步驟 
        #Step 1: Sort: 先按起點排序 (Start time)。
        intervals.sort(key=lambda x: x.start) #list of tuple
        #Step 2:  Iterate to 判斷是否撞車
        for i in range(len(intervals) - 1):
            #撞車-> return False
            if intervals[i].end > intervals[i+1].start:
                return False # 撞車了！
        #Step 3 : Return result
        return True
        '''
        Time Complexity : O (N logN)
            - O (N logN) … … python Merge sort: Divide and conquer
            - O(N)... Traverse size N Array
        Space Complexity - O(1)
            - O(1) …..Create no variable
        '''

















        
