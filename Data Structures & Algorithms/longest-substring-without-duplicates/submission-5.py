class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        #思路： 題目提到「連續子陣列」或「連續子字串」 - 陣列中只有正數
        #題型：Sliding Window題型
        #腦內圖像：滑動窗口的核心是維護一個 [l, r] 的區間，讓 r 不斷向右擴張，當區間不再滿足條件時，讓 l 向右收縮。

        #Step1:  初始化左指針＋res和其他初始值＋state map儲存窗口內的資訊
        start  = 0
        res = 0
        state = {} # {val: count}
        
        #Step2:  For-loop遍遞右指針
        for end in range(len(s)):
            # Step 2-1: 把右邊元素納入窗口,更新 state map
            state[s[end]] = state.get(s[end],0) + 1
            # Step 2-2: 當窗口「違反or滿足條件」時，更新 state map ,收縮左邊
            #有重複
            while state[s[end]] > 1:
                state[s[start]] -= 1
                start+=1
            #Step 2-3: 更新結果 (這時窗口通常是有效的)
            res= max(res,end-start+1)
           
        #Step 3: 回傳結果 
        return res
        

        '''
        Time : O(N)...iterate over the array size N
        Space: O(M)...create size M Map. m is the total number of unique characters ,就要M個key
        '''