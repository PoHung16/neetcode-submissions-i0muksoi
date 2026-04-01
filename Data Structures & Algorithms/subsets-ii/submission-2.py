class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Step 1: sort the list from題目
        nums.sort()
        #Step 2: initialize the final result to store our subsets
        res = []
        #Step 3: define dfs function
        def dfs(i, subset):
            #Step3-1: Base case : when to stop and what should we do
            if i == len(nums):
                res.append(subset.copy())
                return
            # Step3-2: Constraints : 剪支問題
            # Step3-3: Choices with Backtracking: include or not include next element
            # include
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            # not include with constraints
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])
        return res