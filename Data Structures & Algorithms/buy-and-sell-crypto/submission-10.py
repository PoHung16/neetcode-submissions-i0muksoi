"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int , Single Number (max/min profit, cost, ways, jumps)-> DP
"""
# Keyword :  “max/min profit, cost, ways, jumps” or fibonacci sequence ->  Bottom up DP Tabulation - edge cae
# Image :  DP is remembering past results to build the next one, I'll init the base case and dp array/dp varaible, loop through with the transitions formula, and return the final result
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
        min_price = prices[0]
        dp_max_value = 0
        # dp = [0] * n
        for i in range(1,len(prices)):
            dp_max_value = max(prices[i]-min_price, dp_max_value)
            min_price = min(min_price, prices[i]) 
        return dp_max_value
    
    # Time complexity: O(N) ... Traverse size N Array
    # Space complexity:  O(1)....create constant variable

def test():
    sol = Solution()
    result = sol.maxProfit([10,1,5,6,7,1])
    print(f"Result : {result}")

if __name__ == "__main__":
    test()




       
        
        
      
            
        
        

