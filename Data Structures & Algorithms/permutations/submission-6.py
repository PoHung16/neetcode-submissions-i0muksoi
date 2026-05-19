"""
 OOD: No
 Constraints: n <= 20
 input : List[int], int
 output : List[List[int]]
"""
# Keyword : "find all possibilities - Permutation" -> Backtracking (Multi-branch decision tree)
# Image: Define a DFS function that traverse all elements to choose available numbers, tracking the current combination in a subset
# Tricks:
    # 1. Draw a decision tree to help us understand recursive problem
    # 2. DFS need base case to stop - success / fail , and at the end you need to call dfs function
    # 3. permutation backtracking problem you need to use visiited = set() to record if the element has been used before
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def dfs(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for num in nums:
                if num in visited:
                    continue
                subset.append(num)  #move with the  available numbers decision to next level (下層一樣選123)
                visited.add(num)
                dfs(subset)
                subset.pop()
                visited.remove(num)
        dfs([])
        return res


def test():
    sol = Solution()
    nums = [1,2,3]
    result = sol.permute(nums)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()

# Time complexity: O(N * N!)
  # number of nodes: N!
  # copying each subset takes O(N) size time
# Space Complexity: O(N)..... we need to store N dfs recursion stack



