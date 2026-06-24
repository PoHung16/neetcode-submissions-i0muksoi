"""
 OOD: No
 Constraints: No
 input : List[int],int
 output : int
"""
# Keyword : “max/min profit, cost, ways, number, jumps” or fibonacci sequence ->  Bottom up DP Tabulation 
# Image: DP is remembering past results to build the next one, I'll init the base case and dp array/dp varaible, loop through with the transitions formula, and return the final result
# Tricks
    # If the current state only depends on the last one or two steps, you can ditch the dp array and just use dp variables prev2 ,prev1 ,curr to achieve O(1) space
    # If its coin dp problem,cannot use len(coins) as base case, you need to directly build dp array base case
    # If its coin dp problem, dp[i] is used to store how many number of coins to get i value 
    # If its coin dp problem, you will need to loop through the value  one by one and then loop with different coin value with the transitions formula 
    
from typing import List
class Solution:
    def coinChange(self, coins:List[int], amount:int) ->int:
        # edge case
        if not coins:
            return -1
        
        # base case 
        dp = [float("inf")] * (amount+1) # amount+1個value, we need to get fewest way, so start with float("inf")
        dp[0] = 0 # to acheive 0(left) , there is 0 ways(right)

        for i in range(1,amount+1): # 1 to amount
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i], 1+dp[i-coin]) # 狀態轉移：不選這個硬幣(維持 dp[i]) vs 選這個硬幣(這 1 枚硬幣  再加上 dp[i - coin]的方法數)
        return dp[amount] if dp[amount] != float("inf") else -1
        
# Time Complexity: O(S * N)
    # Traverse nested loop :S is amount, N is how many different kind of coins
# Space Complexity: O(S).... create size S+1 Dp array
        

def test():
    sol = Solution()
    result = sol.coinChange([1,5,0],12)
    print(f"Result : {result}")
test()

       








