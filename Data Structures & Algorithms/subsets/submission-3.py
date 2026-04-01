from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Step 1: initialize the final result to store our subsets
        res = []
        subset = []
        #Step 2: define dfs function
        def dfs(i):
            # Step2-1: Base case : when to stop and what should we do
            if i == len(nums):
                res.append(subset.copy())
                return
            # Step2-2: Constraints : None
            # Step2-3: Choices with Backtracking: include or not include next element
            # include
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            #not include -走另一邊
            dfs(i+1)
        
        dfs(0)
        return res
















