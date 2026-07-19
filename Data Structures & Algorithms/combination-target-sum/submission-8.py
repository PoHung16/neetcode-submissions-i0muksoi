"""
 OOD: No
 Constraints: n <= 20 -> Backtracking
 input : List[int],int
 output : List[List[int]]
"""
# Optimal Solution
    # Keyword:  "find all possibility"  -> Basic Backtracking
    # Approach:  Define a DFS function to explore every combination by making a binary choice (include or exclude) for each element
    # Tricks - DFS
        # 1.Draw a decision tree to help us understand recursive problem
        # 2.Procedure: base case -> current level -> next level
    # Tricks - if question may contain duplicates, and you need to avoid it
        # 1. sort it
        # 2. To fast-forward duplicates, check boundary first, then peek if the next one is a twin.
    # Tricks - backtracking
        # 1.If you reuse the number, dfs should stay at the index i
from typing import List
class Solution:
    def combinationSum(self, nums:List[int], target:int) -> List[List[int]]:
        res = []
        def dfs(i,subset,total):
            # base case
            if total == target:
                res.append(subset.copy())   # Without .copy(), python only store a reference to a single list that gets modified and emptied by .pop().
                return
            if i == len(nums) or total > target:
                return
            # current level -pick
            subset.append(nums[i])
            # next level - can pick the same
            dfs(i,subset,total+nums[i])
            # current level - don't pick
            subset.pop()
            # next level 
            dfs(i+1,subset,total)
        dfs(0,[],0)
        return res

# Time complexity: O(H * 2^H)
  # number of nodes: 2^H, H = Total/minumum value in array
  # copying each subset takes O(H) size time
# Space Complexity: O(H)..... we need to store H dfs recursion stack,  H = Total/minumum value in array


def test():
    sol = Solution()
    nums = [2,5,6,9]
    target = 9
    result = sol.combinationSum(nums,target)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()





