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
        # Merge Overlapping and insert newInterval part (s2尾巴不能在s1頭前面) 
        #    S1   S1
        #S2  S2
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max (intervals[i][1],newInterval[1])
            i+=1
        res.append(newInterval)
        #Add Right part
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
    
       
    
        





    
    
    