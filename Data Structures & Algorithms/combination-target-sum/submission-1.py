class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Step 1: initialize the final result to store our subsets
        res = []
        # Step 2: define dfs function,  cur is what value we’ve added to subset
        def dfs(i, cur, total):
            # Step2-1: Base case : when to stop and what should we do
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            #Step2-2: Decision Tree Start : include or not include
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total) # since we do not include, start from i+1
        #Step 3: call dfs function and return result
        dfs(0, [], 0)
        return res