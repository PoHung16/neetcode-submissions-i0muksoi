class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 題型Keyword: "Permutation as a substring" -> Sliding Window (Fixed Size)
        # 腦中圖像: A fixed-size window of length len(s1) sliding across s2.
        # 動作記憶法 - 3個步驟 

        #ps. Edge case
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2 or not n1:
            return False

        #Trick 1：「匹配計數器 (matches)」:建立頻率表, 並計算s1,s2最初字母頻率
        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i])- ord('a')] += 1
            s2Count[ord(s2[i])- ord('a')] += 1
        
        #前i個字母頻率count一樣，代表是permutation, return True
        if s1Count == s2Count:
            return True

        #Trick 2： Sliding Window, 從第i個字母開始，檢查每i length 是不是有permutation
        for i in range(n1,n2):
            #Step 2-1: 把右邊元素納入窗口
            s2Count[ord(s2[i])- ord('a')] += 1
            #Step 2-2: 當窗口「違反or滿足條件」時,收縮左邊
            s2Count[ord(s2[i-n1])- ord('a')] -= 1 #
            #字母頻率count一樣, return True
            if s1Count == s2Count:
                return True
        return False
        