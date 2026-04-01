class Solution:
    def trap(self, height: List[int]) -> int:
        #核心邏輯：
        #1.想像你現在要計算一個山谷能裝多少水。水要留住，一定要有左右兩面牆。
        #A.短板效應：一個水桶能裝多少水，取決於最短的那塊木板。
        #B.為什麼讓「矮的那邊」pointer動？ 假設左邊5米，右邊10米。我們不需要知道右邊中間還有什麼，我們只知道右邊已經有一面 10 米高的牆在那裡守著了
        #對左邊這格的坑來說，能限制它裝水量的「短板」一定是左邊這面 5 米的牆。
        
        #ps. Edge case
        if not height:
            return 0
        #Step1:  初始化左、右指針+ leftMax, RightMax
        l = 0
        r = len(height) -1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        #Step2:  while left< right
        while l < r:
            #Step 2-1: 檢查目前的狀態
            if leftMax < rightMax:
                #Step 2-2: 決定移動哪一個指針
                l = l + 1
                #A.更新leftMax
                leftMax = max(leftMax, height[l])
                #B.同時更新result,  計算當前這一格能接多少水,# 如果這格柱子很高，結果會是 0，代表沒空間接水
                res += leftMax - height[l]
            #Step 2-1: 檢查目前的狀態
            else:
                #Step 2-2: 決定移動哪一個指針
                r = r - 1
                #A.更新leftMax
                rightMax = max(rightMax, height[r])
                #B.同時更新result,  計算當前這一格能接多少水,# 如果這格柱子很高，結果會是 0，代表沒空間接水
                res += rightMax - height[r]
        # 當 l 和 r 相遇，代表整個地圖都掃描完了
        return res





        