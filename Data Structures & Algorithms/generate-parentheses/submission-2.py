"""
 OOD: No
 Constraints: n <= 20
 input : List[int]
 output : List[List[int]]
"""
# Keyword : "find all possibility"  -> Basic Backtracking
# Image:
    #1. Define a DFS function to choose or not choose the i-th number, tracking the current combination in a subset and target(if needed)
    #2. If the question is Return all well-formed parentheses, you Define a DFS function to choose "(" or ")" for the current position, tracking the current combination string 
# Tricks:
    # 1. Draw a decision tree to help us understand recursive problem
    # 2. DFS need base case to stop - success / fail , and at the end you need to call dfs function
    # 3. DFS sometimes will have constraints, openN < n + closedN < openN
    # 4. If you reuse the number, dfs should stay at the index i
    # 5. If the question contain duplicates, and you need to return unique combinations-> sort it first and skip the same element,
        #  while i+1 < len(candidates)..avoid index error and candidates[i+1] == candidates[i]:i+=1
    # 6. ("").join(list) -> it will concatenate all list element into a string

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openN,closedN,subset):
            if openN == closedN == n:
                res.append("".join(subset))
                return
            if openN < n:
                subset.append("(")
                dfs(openN+1, closedN, subset)
                subset.pop()
            if closedN < openN:
                subset.append(")")
                dfs(openN, closedN+1, subset)
                subset.pop()
            
        dfs(0, 0,[])
        return res

def test():
    sol = Solution()
    n = 1
    result = sol.generateParenthesis(n)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()


# Time complexity: O(N * Cn)
  # number of valid nodes/subsets: bounded by Catalan Number (Cn) due to smart pruning.
  # copying / joining each subset takes O(n) size time
# Space Complexity: O(n)..... we need store 2N dfs recursion stack as height

#第 4 層: dfs(2, 2) <-- 觸發 Base Case，把 "(())" 存進 res！
#第 3 層: dfs(2, 1)
#第 2 層: dfs(2, 0)
#第 1 層: dfs(1, 0)
#第 0 層: dfs(0, 0)

