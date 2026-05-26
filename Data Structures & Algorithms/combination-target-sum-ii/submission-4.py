"""
 OOD: No
 Constraints: n <= 20
 input : List[int], int
 output : List[List[int]]
"""
# Keyword : "find all possibility"  -> Basic Backtracking
# Image: Define a DFS function to choose or not choose the i-th number, tracking the current combination in a subset and target(if needed)
# Tricks:
    # 1. Draw a decision tree to help us understand recursive problem
    # 2. DFS need base case to stop - success / fail , and at the end you need to call dfs function
    # 3. If you reuse the number, dfs should stay at the index i
    # 4. If the question contain duplicates, and you need to return unique combinations-> sort it first and skip the same element,
        #  while i+1 < len(candidates)..avoid index error and candidates[i+1] == candidates[i]:i+=1


class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i,subset,total):
            if total == target:
                res.append(subset.copy())
                return
            if i==len(nums) or total > target:
                return
            subset.append(nums[i])
            dfs(i+1,subset,total+nums[i])
            subset.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            dfs(i+1,subset,total)
        dfs(0,[],0)
        return res
def test():
    sol = Solution()
    candidates = [9,2,2,4,6,1,5]
    target = 8
    result = sol.combinationSum2(candidates,target)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()

# Time complexity: O(N * 2^N)
  # sorting: NlogN ... divide and conquer
  # number of nodes: 2^N
  # copying each subset takes O(N) size time
# Space Complexity: O(N)..... we need to store N dfs recursion stack




