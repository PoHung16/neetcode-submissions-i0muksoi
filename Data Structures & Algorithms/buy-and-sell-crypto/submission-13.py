"""
 OOD: No
 Constraints: No
 Input : List[int]
 Output :Single Number(max/min profit, cost, ways, jumps or fibonacci sequence) ->DP
"""
# Brute Force: 
    # : Array - Use nested loops to check the profit for every possible pair and update the maximum profit -> O(N^2)
class Solution:
    def maxProfit(self, prices:List[int])->int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit,profit)
        return max_profit

# Optimal Solution
    # Goal : O(N^2) -> O(N)
    # Keyword:  “max/min profit, cost, ways, jumps” or fibonacci sequence ->  Bottom up DP  - edge cae
    # Approach:  DP is remembering past results to build the next one, I'll init the base case and dp array/dp varaible to  remember each position's maximum profit, traverse the array to update dp variable, and return the final result
    # Tricks:
       # If the current state only depends on the last one or two steps, you can ditch the dp array and just use dp variables - prev, curr  to achieve O(1) space

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case
        if not prices:
            return 0
        # base case
        if len(prices)==1:
            return 0
        dp_variable = 0  # remember maximum profit for each position, dp variable only depends on only one step
        min_price = prices[0]
        for i in range(len(prices)):
            dp_variable =  max(prices[i]-min_price, dp_variable)
            min_price = min(prices[i],min_price)
        return dp_variable
        
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(1)....create constant variable

def test():
    sol = Solution()
    result = sol.maxProfit([10,1,5,6,7,1])
    print(f"Result : {result}")

if __name__ == "__main__":
    test()




       
        
        
      
            
        
        










