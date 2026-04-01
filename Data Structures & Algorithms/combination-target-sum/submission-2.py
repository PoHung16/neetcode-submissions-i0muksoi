class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Step 1: initialize the final result to store our subsets
        res = []
        # Step 2:  define dfs function - dfs(i,subset,total)
        def dfs(i, subset, total):
            # Step2-1: Base case : when to stop and what should we do
            if total == target:
                res.append(subset.copy())
                return
            if i == len(nums) or total > target:
                return
            #Step2-2: Constraints : None
            #Step2-3: Choices with Backtracking: include or not include current or next element
            #include
            subset.append(nums[i])
            dfs(i, subset, total + nums[i])
            subset.pop()
            #not include
            dfs(i + 1, subset, total) # since we do not include, start from i+1
        #Step 3: call dfs function and return result
        dfs(0, [], 0)
        return res