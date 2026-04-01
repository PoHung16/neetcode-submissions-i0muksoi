class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Step 1: 初始化左指針＋res和其他初始值＋statemap
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




