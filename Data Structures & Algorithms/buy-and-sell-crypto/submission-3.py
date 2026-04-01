class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 題型Keyword:  “max/min profit, cost, ways, jumps” ->  Bottom up DP Tabulation / DP Constant
        # 腦中圖像:  we only need the previous answer to find the current answer , we use dynamic programming to store the answer for the sub problem 
        # 動作記憶法 - 三個步驟
        # ps.Edge case
        if not prices or len(prices) < 2: 
            return 0
        # Step1: Base Case + Initialize DP Tabulation Array  or Initialize DP variable (if dp[i] only need less than 2 steps to get inferred)
        dp_maxium_profit = 0
        min_price = prices[0] #we need min_price to calcuate maxium profit
        # Step 2: Traverse DP array with state transition formula
        for i in range(len(prices)):
            min_price = min(min_price,prices[i] )
            dp_maxium_profit = max(dp_maxium_profit, prices[i]-min_price )
        
        #Step 3 return result
        return dp_maxium_profit


# Time Complexity: O(n)....traverse n array
# Space Complexity: O(1).... constant space
def test():
    sol = Solution()
    result = sol.maxProfit([10,1,5,6,7,1])
    print(f"Result : {result}")
test()


        
        
          


       
        
        
      
            
        
        

