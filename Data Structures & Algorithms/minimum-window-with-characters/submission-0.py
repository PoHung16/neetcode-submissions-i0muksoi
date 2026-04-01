class Solution:
    def minWindow(self, s: str, t: str) -> str:
    

        # Step 1: 初始化
        # 初始化左指針 (l) + 結果紀錄 (res, resLen)
        # statemap 儲存窗口內的資訊 (window) 與 目標資訊 (countT)
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        # Step 2: For-loop 遍歷右指針 (r)
        for r in range(len(s)):
            # Step 2-1: 把右邊元素納入窗口, 更新 window 資訊
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # 更新達標狀態 (state)
            if c in countT and window[c] == countT[c]:
                have += 1

            # Step 2-2: 當窗口「滿足條件」(湊齊 T) 時，收縮左邊
            while have == need:
                # Step 2-3: 更新結果 (因為是求 Minimum，在有效時更新)
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # 移除左邊元素，並更新 state 資訊
                char_to_remove = s[l]
                window[char_to_remove] -= 1
                
                # 如果移除後導致該字元「不達標」，則 have 減少
                if char_to_remove in countT and window[char_to_remove] < countT[char_to_remove]:
                    have -= 1
                
                # 左指針右移，嘗試找更短的
                l += 1
        
        # Step 3: 回傳結果 (根據紀錄的座標切字串)
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""