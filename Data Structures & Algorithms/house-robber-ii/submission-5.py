"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Keyword : “max/min profit, cost, ways, jumps” or fibonacci sequence ->  Bottom up DP Tabulation 
# Image: DP is remembering past results to build the next one, I'll init the base case and dp array/dp varaible, loop through with the transitions formula, and return the final result
# Tricks
    # If the current state only depends on the last one or two steps, you can ditch the dp array and just use dp variables  to achieve O(1) space
    #  if Dp array is a circle, you calcuate dp twice - one from 1: n, the other from 0:-1

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case
        if not nums:
            return 0
        # Base case
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        n = len(nums)
        return max(self.rob_liner(nums[1:n]), self.rob_liner(nums[0:-1]))
            
       
    
    def rob_liner(self, nums: List[int]) -> int:
        # Edge case
        if not nums:
            return 0
        # Base case
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        prev = nums[0]
        curr = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            prev , curr = curr, max(prev+nums[i], curr)

        return curr

   
# Time Complexity: O(n)....traverse size n array
# Space Complexity: O(1).... constant space
def test():
    sol = Solution()
    result = sol.rob([3,4,3])
    print(f"Result : {result}")
test()

       


        