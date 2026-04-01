class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 題型Keyword:  “Minimum Operations”
        # 腦中圖像:  “活動計劃“ ->兩個活動時間重疊時，砍掉「結束較晚」的那個，因為它最佔時間，這樣我們可以塞更多活動
        # 動作記憶法 - 三個步驟 
        #Step 1: Sort by END 並記錄上一個活動結束時間 (貪心排序)
        intervals.sort(key=lambda x:x[1])
        prev_end = intervals[0][1]
        count = 0
        #Step 2: Iterate from 2nd interval 判斷是否砍掉活動
        for i in range(1,len(intervals)):
            # 重疊-> 砍掉比較晚結束的那個活動(which is the current one),不更新上一個活動結束時間
            if prev_end > intervals[i][0]:
                count +=1
            #沒重疊-> 更新上一個活動結束時間
            else:
                prev_end = intervals[i][1]
        #Step 3 : Return result
        return count

        #[1,2][3,5][2,6]

        '''
        Time Complexity : O (N logN)
            - O (N logN) … … python Merge sort: Divide and conquer
            - O(N)... Traverse size N Array
        Space Complexity - O(1)
            - O(1) …..Create no variable
        '''
        