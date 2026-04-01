class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        #Step1:  初始化左指針＋res和其他初始值＋state map儲存窗口內的資訊
        seen = {}
        res = 0
        start = 0
        #Step2:  For-loop遍遞右指針
        for end in range(len(s)):
            # Step 2-1: 把右邊元素納入窗口,更新 state map
            seen[s[end]] = seen.get(s[end], 0) + 1
            # Step 2-2: 當窗口「違反or滿足條件」時，收縮左邊,更新 state map
            while seen[s[end]] > 1:
                seen[s[start]] -= 1
                start += 1
            #Step 2-3: 更新結果 (這時窗口通常是有效的)
            res = max(res, end - start + 1)
        return res
