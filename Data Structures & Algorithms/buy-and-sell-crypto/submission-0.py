class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Step1:  初始化左指針＋res和其他初始值＋state儲存窗口內的資訊
        l = 0 # 買入日
        res = 0
        #Step2:  For-loop遍遞右指針
        for r in range(len(prices)): # r 是賣出日
            #Step 2-1: 把右邊元素納入窗口, 更新 state
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            #Step 2-2: 當窗口「違反or滿足條件」時，收縮左邊
            else: # 如果賣出日價格比買入日還低，這天就是新的買入起點
                l = r 
        return res