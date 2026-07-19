"""
 OOD: No
 Constraints: n <= 20 -> Backtracking
 input : List[int]
 output : List[List[int]]
"""
# Optimal Solution
    # Keyword:  "find all possibility"  -> Basic Backtracking
    # Approach:  Define a DFS function to  explore every combination by making a binary choice (include or exclude) for each element
    # Tricks - DFS
        # 1.Draw a decision tree to help us understand recursive problem
        # 2.Prcedure: base case -> current level -> next level

class Solution:
    def subsets(self, nums:List[int])->List[List[int]]:
        res = []
        def dfs(i,subset):
            # base case
            if i==len(nums):
                res.append(subset.copy()) # Without .copy(), python only store a reference to a single list that gets modified and emptied by .pop().
                return
            # current level -pick
            subset.append(nums[i])
            # next level
            dfs(i+1,subset)
            # current level - don't pick
            subset.pop()
            # next level
            dfs(i+1,subset)
        dfs(0,[])
        return res

# Time complexity: O(N * 2^N)
  # number of nodes: 2^N  possible subsets
  # copying each subset takes O(n) size time
# Space Complexity: O(n)..... we need store N dfs recursion stack as height

 
def test():
    sol = Solution()
    nums = [1,2,3]
    result = sol.subsets(nums)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()












