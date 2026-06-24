"""
 OOD: No
 Constraints: No
 input : int
 output : int
"""
# Keyword : “max/min profit, cost, ways, jumps” or fibonacci sequence ->  Bottom up DP Tabulation 
# Image: DP is remembering past results to build the next one, I'll init the base case and dp array/dp varaible, loop through with the transitions formula, and return the final result
# Tricks
    # If the current state only depends on the last one or two steps, you can ditch the dp array and just use dp variables  to achieve O(1) space


class Solution:
    def climbStairs(self, n: int) -> int:
        # edge case
        if not n:
            return 0
        # base case
        if n==1:
            return 1
        if n==2:
            return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n-1]

# Time Complexity: O(n)....traverse n array
# Space Complexity: O(1).... constant space

def test():
    sol = Solution()
    result = sol.climbStairs(2)
    print(f"Result : {result}")
test()









