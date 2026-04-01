class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Ps.看有沒有edge case, return false
        if not nums:
            return 0
        #Step1: 創建一個Dp Array with Initialized Value with size N. Dp為題目本身問的東西,dp[i]為 第i個位置的LIS
        #Initialize Base Case
        n = len(nums)
        dp = [1] * n
        #Step2: For Loop To Fill out Dp Array 
        for i in range(n):
            #Step 2-1: 狀態轉移方程 - 後面可以從前面推得
            for j in range(i):
                if nums[i] > nums[j]:  #現在的數>之前的某一個數
                    dp[i] = max(dp[i],dp[j]+1)
        #Step 3:回傳dp Array Last 最大值
        return max(dp)


        