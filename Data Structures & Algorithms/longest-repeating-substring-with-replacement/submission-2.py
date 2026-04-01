class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Step1:  初始化左指針＋res和其他初始值＋statemap儲存窗口內的資訊
        state = {}
        start = 0
        res = 0
        max_frequency = 0 
        #Step2:  For-loop遍遞右指針
        for end in range(len(s)):
            #Step 2-1: 把右邊元素納入窗口,更新 state map
            state[s[end]] = state.get(s[end],0) + 1
            max_frequency = max(max_frequency, state[s[end]])
            #Step 2-2: 當窗口「違反or滿足條件」時，移除state,收縮左邊
            # 如果 (窗口長度 - 最高頻率字母) > k，代表替換不了，窗口必須右移
            while (end - start + 1) - max_frequency > k:
                state[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        #Step 3: 回傳結果
        return res



