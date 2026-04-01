class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #思路：最長子序列與子字串：涉及不連續的長度比較
        #題型：
        #Bottom Up DP - tabulation :後面可以從前面推得
        #如果dp[i] 只跟 dp[i-1] 有關 -> 空間壓縮

        #Ps.看有沒有edge case, return false
        if not prices: 
            return 0
        #Step1: 創建一個Dp Variable(max_profit) + min_price
        #Step2: Initialize Base Case
        min_price = prices[0]
        max_profit = 0
        #Step3: For Loop To Fill out Dp Variable 
        for i in range(len(prices)):
            #Step 3-1: 更新min_price
            min_price = min(min_price, prices[i])
            #Step 3-1: 狀態轉移方程 - 後面可以從前面推得
            max_profit = max(max_profit, prices[i]-min_price )
        #Step4:回傳dp Array Last 最大值
        return max_profit

