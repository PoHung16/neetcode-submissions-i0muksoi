class Solution:
    def longestPalindrome(self, s: str) -> str:
        #題型Keyword: “Palindrome” 
        #腦中圖像: Opposite pointer左右靠近 
        #動作記憶法 - 三個步驟 
        #Ps. Edge case
        if not s: return ""
        res = ""
        res_len = 0   
        # Step 1 : Expand the center to the longest Palindrome by 2 opposite pointer
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # 停止時，l 和 r 多跑了一步，所以回傳 s[l+1 : r]

        # Step 2: Traverse all possible center to expand
        for i in range(len(s)):
            #Step 2-1: 奇數中心擴散 (e.g., "aba"), 代表 l 和 r 一開始都指在同一個字元上
            s1 = expand(i, i)
            # Step 2-2: 偶數中心擴散 (e.g., "abba"), 因為中心點不是一個字元，而是這兩個相鄰字元。
            s2 = expand(i, i + 1)
            # Step 2-3: 更新全局最長的結果 
            if len(s1) > res_len:
                res = s1
                res_len = len(s1)
            if len(s2) > res_len:
                res = s2
                res_len = len(s2)
        #Step 3: 回傳結果
        return res




