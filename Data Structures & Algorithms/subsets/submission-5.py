"""
 OOD: No
 Constraints: n <= 20
 input : List[int]
 output : List[List[int]]
"""
# Keyword : "find all possibility"  -> Basic Backtracking
# Image: Define a DFS function to choose or not choose the i-th number, tracking the current combination in a subset.(python is sharing same memory address, you need to use copy for its content)
# Tricks:
    # 1. Draw a decision tree to help us understand recursive problem
    # 2. DFS need base case to stop , and at the end you need to call dfs function
    
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i,subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            dfs(i+1,subset)
        dfs(0,[])
        return res
def test():
    sol = Solution()
    nums = [1,2,3]
    result = sol.subsets(nums)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()


# Time complexity: O(N * 2^N)
  # number of nodes: 2^N  possible subsets
  # copying each takes O(n) time
# Space Complexity: O(n)..... we need store N dfs recursion stack







