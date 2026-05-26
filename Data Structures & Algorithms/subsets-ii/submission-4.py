"""
 OOD: No
 Constraints: n <= 20
 input : List[int]
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
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,subset):
            if i==len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            dfs(i+1,subset)
        dfs(0,[])
        return res

def test():
    sol = Solution()
    nums = [1,2,1]
    result = sol.subsetsWithDup(nums)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()

# Time complexity: O(N * 2^N)
  # number of nodes: 2^N  possible subsets, no duplicates
  # copying each subset takes O(n) size time
# Space Complexity: O(n)..... we need store N dfs recursion stack as height










