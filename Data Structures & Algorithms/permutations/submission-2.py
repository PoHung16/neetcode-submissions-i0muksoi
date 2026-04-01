class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Step 1: initialize the final result to store our subsets
        res = []
        #Step 2: define dfs function : def dfs(subset)
        def dfs(subset):
            #Step2-1: Base case : when to stop and what should we do
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                # Step2-2: Constraints : Can not use the same number more than once in our path
                if nums[i] in subset:
                    continue
                #Step2-3: Choices with Backtracking: include other element in array besides it self
                #include
                subset.append(nums[i])
                dfs(subset)
                subset.pop()
        #Step 3: call dfs function and return result
        dfs([])
        return res