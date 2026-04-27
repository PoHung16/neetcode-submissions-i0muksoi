"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int , Single Number (max/min profit, cost, ways, jumps)-> DP
"""
# Keyword :  “max/min profit, cost, ways, jumps” or fibonacci sequence ->  Bottom up DP Tabulation 
# Image :  DP is remembering past results to build the next one,I'll init the base case, loop through the transitions, and return the final result
# Tricks:
   #If the current state only depends on the last one or two steps, you can ditch the array and just 'slide' variables forward to achieve O(1) space

class Solution:
    def maxProfitArray(self, prices: List[int]) -> int:
        if not prices:
            return 0
        if len(prices)<2:
            return 0
        dp = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i]) # Update the lowest price seen so far
            dp[i] = max(dp[i-1], prices[i] - min_price) #Max profit is either previous max OR (current - min)
        return dp[-1]
    
    # Time complexity: O(N) ... Traverse size N Array
    # Space complexity:  O(N)....create size N Array

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        if len(prices)<2:
            return 0
        min_price = prices[0]
        dp_maxium_profit = 0
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i]) # Update the lowest price seen so far
            dp_maxium_profit = max(dp_maxium_profit, prices[i] - min_price) #Max profit is either previous max OR (current - min)
        return dp_maxium_profit
    
    # Time Complexity: O(n)....traverse size array
    # Space Complexity: O(1).... constant space 

def test():
    sol = Solution()
    result = sol.maxProfit([10,1,5,6,7,1])
    print(f"Result : {result}")

if __name__ == "__main__":
    test()




       
        
        
      
            
        
        

