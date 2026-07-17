"""
 OOD: No
 Constraints: No
 input : List[int]
 output : boolean
"""
from typing import List
# Brute Force: 
    # Use recursion to try every possible jump from the current index to see if any path reaches the end -> O((max)^N) -> every step have max options
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        def can_reach(i):
            # Base case: If we reach or pass the last index, we succeed
            if i >= n - 1:
                return True
            # Current level work: Try every single jump length allowed from position i
            for jump in range(1, nums[i]+1): #往前幾格
                if can_reach(i+jump):
                    return True
            return can_reach(0)


# Optimal Solution
    # Keyword:  "Maximum Subarray", "Contiguous Sum", "Jump Game" -> Greedy (Decide optimally at each step using a single state/target variable to reach the global best)
    # Approach: Maintain a single running target variable. At each step, greedily update the varible if it becomes negative/ if it can reach to this position. 
    # Tricks:
        # Jump games:  Start from the last index and move backward. variable representing the closest reachable milestone

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start from the end
        # Time : O(N)
        # Space: O(1)
        n = len(nums)
        target = n-1
        for i in range(n-1,-1,-1):
            max_jump = nums[i]
            if i + max_jump >= target:
                target = i
        return target ==0
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(1) ... Only constant variable

        
def test():
    sol = Solution()
    
    nums1 = [1, 2, 0, 1, 0]
    result1 = sol.canJump(nums1)
    print(f"result1: {result1}") # Expected output: True
    
    nums2 = [1, 2, 1, 0, 1]
    result2 = sol.canJump(nums2)
    print(f"result2: {result2}") # Expected output: False

if __name__ == "__main__":
    test()