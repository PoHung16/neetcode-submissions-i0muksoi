class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #Step 1: initialize the final result to store our subsets
        res = []
        #Step 2: define dfs function : def dfs(permutation)
        def dfs(permutation):
            #Step2-1: Base case : when to stop and what should we do
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            # Step2-2: Decision Tree Start : include for every index,到底跳回去,不往下走
            for i in range(len(nums)):
                if nums[i] in permutation:
                    continue
                #include
                permutation.append(nums[i])
                dfs(permutation)
                #跳回去,不往下走
                permutation.pop()
        
        dfs([])
        return res