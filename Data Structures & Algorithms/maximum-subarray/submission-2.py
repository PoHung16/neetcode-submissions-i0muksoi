"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Brute Force: 
    # Use nested loop to check every possible subarray sum from index i to j -> O(N^2)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i,len(nums)):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        return max_sum

# Optimal Solution
    # Keyword:  "Maximum Subarray", "Contiguous Sum" -> Greedy (Decide optimally at each step using a single state variable to reach the global best)
    # Approach: Maintain a single running sum variable. At each step, greedily drop the previous sum if it becomes negative. This localized optimal choice directly leads to the global maximum result.
from typing import List
class Solution:
    def maxSubArray(self, nums:[List[int]])->int:
        max_sum = float("-inf")
        current_sum = 0 
        for i in range(len(nums)):
            current_sum += nums[i]
            max_sum =  max(max_sum,current_sum)
            if current_sum < 0:
                current_sum = 0
        return max_sum

# Time complexity: O(N) ... Traverse size N
# Space complexity:  O(1) ... Only constant variable

def test():
    sol = Solution()
    nums = [2,-3,4,-2,2,1,-1,4]
    result = sol.maxSubArray(nums)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


