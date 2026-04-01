class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Step 1: sort the list from題目
        candidates.sort()
        # Step 2: initialize the final result to store our subsets
        res = []
        # Step 3: define dfs function
        def dfs(i, subset, total):
            #Step3-1: Base case : when to stop and what should we do
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i == len(candidates):
                return
            # Step3-2: Constraints :  剪支問題
            # Step3-3: Choices with Backtracking include or not include  next element
            # include
            subset.append(candidates[i])
            dfs(i + 1, subset, total + candidates[i])
            subset.pop()
            # not include
            while i + 1 < len(candidates) and candidates[i+1] ==  candidates[i]:
                i += 1
            dfs(i + 1, subset, total)

        dfs(0, [], 0)
        return res