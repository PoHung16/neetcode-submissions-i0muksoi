"""
 OOD: No
 Constraints: n <= 20 -> Backtracking
 input : List[int]
 output : List[List[int]]
"""
# Optimal Solution
    # Keyword:  "find all possibility"  -> Basic Backtracking
    # Approach:  Define a DFS function to explore every combination by making a binary choice (include or exclude) for each element
    # Tricks - DFS
        # 1.Draw a decision tree to help us understand recursive problem
        # 2.Procedure: base case -> current level -> next level
    # Tricks - if question may contain duplicates, and you need to avoid it
        # 1.sort it
        # 2. To fast-forward duplicates, check boundary first, then peek if the next one is a twin.

from typing import List
class Solution:
    def subsetsWithDup(self, nums:[List[int]]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,subset):
            # base case
            if i==len(nums):
                res.append(subset.copy())  # Without .copy(), python only store a reference to a single list that gets modified and emptied by .pop().
                return 
            # current level -pick
            subset.append(nums[i])
            # next level
            dfs(i+1,subset)
            # current level - don't pick
            subset.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            # next level
            dfs(i+1,subset)
        dfs(0,[])
        return res


# Time complexity: O(N * 2^N)
  # Sort: O(NlogN) ...divide & conquer
  # number of nodes: 2^N  possible subsets, no duplicates
  # copying each subset takes O(n) size time
# Space Complexity: O(n)..... we need store N dfs recursion stack as height

def test():
    sol = Solution()
    nums = [1,2,1]
    result = sol.subsetsWithDup(nums)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


