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

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return
            if i == len(nums) or total > target:
                return
            subset.append(nums[i])
            dfs(i, subset, total + nums[i]) 
            subset.pop()
            dfs(i + 1, subset, total) 
        dfs(0, [], 0)
        return res

def test():
    sol = Solution()
    nums = [2,5,6,9]
    target = 0
    result = sol.combinationSum(nums,target)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()

# Time complexity: O(N * 2^H)
  # number of nodes: 2^H, H = Total/minumum value in array
  # copying each subset takes O(H) size time
# Space Complexity: O(n)..... we need store N dfs recursion stack





