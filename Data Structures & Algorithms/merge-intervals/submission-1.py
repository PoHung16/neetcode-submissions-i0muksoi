class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #題型Keyword: “Merge”, “Insert”
        #腦中圖像:  “貪吃蛇“ -> 後面的頭如果撞到前面的尾，就把前面的尾巴拉長。
        #動作記憶法 - 三個步驟 
        #Step 1: Sort: 先按起點排序 (Start time)。
        intervals.sort(key=lambda x:x[0]) #key= 接一個函數，lambda為匿名函數， take x : return x[0] 
        res = []
        #Step 2:  Iterate to build res
        for i in range(len(intervals)):
            #[1,3] [4,5]
            #不重疊 -> append 進結果
            if not res or res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            #重疊-> Merge Interval
            else:
                res[-1][1] = max(intervals[i][1],res[-1][1])
        #Step 3 : Return result
        return res
        
        '''
        Time Complexity : O (N logN)
            - O (N logN) … … python Merge sort: Divide and conquer
            - O(N)... Traverse size N Array
        Space Complexity - O(N)
            - O(N) ….Create Size N List
        '''








        

        

        