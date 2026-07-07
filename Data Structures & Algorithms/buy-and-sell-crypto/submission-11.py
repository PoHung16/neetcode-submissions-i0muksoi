"""
 OOD: No
 Constraints: No
 input : List[int]
 output :Single Number(max/min profit, cost, ways, jumps or fibonacci sequence) ->DP
"""
# Brute Force: 
    # : Use nested loops to check the profit for every possible pair -> O(N^2)
class Solution:
    def maxProfit(self, prices:List[int])->int:
        max_profit = 0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit,profit)
        return max_profit
# Optimal Solution
    # Keyword:  “max/min profit, cost, ways, jumps” or fibonacci sequence ->  Bottom up DP Tabulation - edge cae
    # Approach:  dp[i] is remembering past results(maximum) from day 0 to day[i]
    # Tricks:
       # DP = edge case + base case + transistion formula compare previous dp result & current result
       # If the current state only depends on the last one or two steps, you can ditch the dp array and just use dp variables - prev, curr  to achieve O(1) space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case
        if not prices:
            return 0
        # base case
        if len(prices)==1:
            return 0
        min_price = prices[0]
        dp_max_value = 0
        # dp = [0] * n
        for i in range(1,len(prices)):
            min_price = min(min_price, prices[i]) 
            # dp[i] = max(prices[i]-min_price,dp[i-1])
            dp_max_value = max(prices[i]-min_price, dp_max_value)
            
        return dp_max_value
    
    # Time complexity: O(N) ... Traverse size N Array
    # Space complexity:  O(1)....create constant variable

def test():
    sol = Solution()
    result = sol.maxProfit([10,1,5,6,7,1])
    print(f"Result : {result}")

if __name__ == "__main__":
    test()




       
        
        
      
            
        
        

