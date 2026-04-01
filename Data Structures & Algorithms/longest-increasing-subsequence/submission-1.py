class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #思路:最長子序列與子字串：涉及不連續的長度比較 
        #題型：Bottom Up DP - tabulation :後面可以從前面推得(有時候可以用constant Space)
        #Ps.看有沒有edge case, return false
        if not nums:
            return 0
        n = len(nums)
        #Step1: 創建一個Dp Array with Initialized Value with size N. Dp為題目本身問的東西
        #dp[i]為 第i個位置的LIS
        #Step2: Initialize Base Case-None
        dp = [1] * n

        #Step3: For Loop To Fill out Dp Array 
        # ex : 1,3,6,7,9,4,10,5,6
        for i in range(n):
            #Step 3-1: 狀態轉移方程 - 後面可以從前面推得
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        #Step 3:回傳dp Array Last 最大值
        return max(dp)



        
        

        