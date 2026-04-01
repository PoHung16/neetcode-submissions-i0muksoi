class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Step 1: sort the list from題目
        nums.sort()
        #Step 2: initialize the final result to store our subsets
        res = []
        #Step 3: define dfs function
        def backtrack(i, subset):
            #Step3-1: Base case : when to stop and what should we do
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res