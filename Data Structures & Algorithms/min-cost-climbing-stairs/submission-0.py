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

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Base case
        if not cost:
            return 0
        if len(cost)== 1:
            return cost[0]
        if len(cost)==2:
            return min(cost[0], cost[1])
        
        # prev2 represents the minimum cost to start from step i-2
        # prev1 represents the minimum cost to start from step i-1
        prev2 = cost[0]
        prev1 = cost[1]

        # Iterate from index 2 up to the last index of the array
        for i in range(2, len(cost)):
            # Total cost to start from  the current step
            curr = cost[i] + min(prev1, prev2)
            # Shift our pointers forward for the next iteration
            prev2, prev1 = prev1, curr
            
        # To get past the top of the stairs, we take the minimum start from the last two steps
        return min(prev1, prev2)

# Time Complexity: O(n)....traverse size n array
# Space Complexity: O(1).... constant space

def test():
    sol = Solution()
    cost = [1,2,3]
    result = sol.minCostClimbingStairs(cost)
    print(f"Result : {result}")
test()
        