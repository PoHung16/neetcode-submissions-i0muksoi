class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #思路： 本質上你在尋找一個「區間」or 題目提到「連續子陣列」或「連續子字串」。 
        #Sliding Window題型
        # Step1: 初始化
        #左指針
        #Res : 座標地圖＋最短長度紀錄
        #Statemap儲存窗口內的資訊 +targetMap儲存目標資訊並初始化
        #條件判斷標準元素
        #need : # 目標種類數
        #Have : # 目前達標種類數
        start = 0
        res_range = [-1, -1]       # 座標地圖
        res_len = float('inf')     # 最短長度紀錄
        stateMap = {}           # 儲存窗口內的資訊
        targetMap = {}                # 儲存目標資訊
        for c in t:
            targetMap[c] = targetMap.get(c, 0) + 1
            
        need = len(targetMap)         # 目標種類數
        have = 0                   # 目前達標種類數
        
        # Step 2: For-loop 遍歷右指針 
        for end in range(len(s)):
            # Step 2-1: 把右邊元素納入窗口把右邊元素納入窗口,更新 state map , 條件判斷標準元素
            stateMap[s[end]] = stateMap.get(s[end], 0) + 1
            if s[end] in targetMap and stateMap[s[end]] == targetMap[s[end]]:
                have += 1
            
            # Step 2-2: 當窗口「滿足條件」時，更新結果 (這時窗口通常是有效的)
            while have == need:
                #新窗口更小的話
                if (end - start + 1) < res_len:
                    res_range = [start, end]
                    res_len = end - start + 1
            
                # Step 2-3: 移除 state map,收縮左邊移除 state map,條件判斷標準元素,收縮左邊
                stateMap[s[start]] -= 1
                if s[start] in targetMap and stateMap[s[start]] < targetMap[s[start]]:
                    have -= 1
                
                start += 1
        
        # Step 3: 回傳結果 (根據座標切字串)
        start, end = res_range
        return s[start : end + 1] if res_len != float("inf") else ""




