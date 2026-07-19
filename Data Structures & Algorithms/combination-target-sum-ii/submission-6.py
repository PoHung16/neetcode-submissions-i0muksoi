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
    def combinationSum2(self, nums:List[int], target:int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,subset,total):
            # base case
            if total == target:
                res.append(subset.copy())   # Without .copy(), python only store a reference to a single list that gets modified and emptied by .pop().
                return
            if i == len(nums) or total > target:
                return
            # current level -pick
            subset.append(nums[i])
            # next level - cannot pick the same
            dfs(i+1,subset,total+nums[i])
            # current level - don't pick
            subset.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            # next level 
            dfs(i+1,subset,total)
        dfs(0,[],0)
        return res
# Time complexity: O(N * 2^N)
  # Sort: O(NlogN) ...divide & conquer
  # number of nodes: 2^N  possible subsets, no duplicates
  # copying each subset takes O(n) size time
# Space Complexity: O(n)..... we need store N dfs recursion stack as height


def test():
    sol = Solution()
    nums = [2,5,6,9]
    target = 9
    result = sol.combinationSum2(nums,target)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()






# Time complexity: O(N * 2^N)
  # sorting: NlogN ... divide and conquer
  # number of nodes: 2^N
  # copying each subset takes O(N) size time
# Space Complexity: O(N)..... we need to store N dfs recursion stack




