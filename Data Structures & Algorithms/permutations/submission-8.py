"""
 OOD: No
 Constraints: n <= 20 -> Backtracking
 input : List[int]
 output : List[List[int]]
"""

# Optimal Solution
    # Keyword:  "find all possibility" -> Backtracking 
    # Approach: Define a DFS function to build permutations. At each position, loop through all elements in nums. If an element hasn't been used yet, pick it, mark it as used, and move to the next position.
    # Tricks - DFS
        # 1.Draw a decision tree to help us understand recursive problem
        # 2.Procedure: base case -> current level -> next level
    # Tricks - Permutations
        # 1. Use a 'visited' set to track which elements are already in the current path.
        # 2. Traverse all elements in nums at EVERY level, skipping visited ones.
        # 3. For loop automatically handles the "don't pick" branch to next level by moving to the next element
from typing import List
class Solution:
    def permute(self, nums:List[int])->List[List[int]]:
        visited = set()
        res = []
        def dfs(subset):
            # base case
            if len(subset) == len(nums):
                res.append(subset.copy())  # Without .copy(), python only store a reference to a single list that gets modified and emptied by .pop().
                return
            # current level
            for num in nums:
                if num in visited:
                    continue
                # current level - pick
                subset.append(num)
                visited.add(num)
                # next level
                dfs(subset)
                # current level - not pick
                subset.pop()
                visited.remove(num)
        dfs([])
        return res   

# Time complexity: O(N * N!)
  # number of nodes: N! (factorial) total permutations at the leaf level
  # copying each subset takes O(N) time
# Space Complexity: O(N) ... we need to store N dfs recursion stack as height, and visited set takes O(N) space
def test():
    sol = Solution()
    nums = [1,2,3]
    result = sol.permute(nums)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()


