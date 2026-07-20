"""
 OOD: No
 Constraints: n <= 20 -> Backtracking
 input : int
 output : List[List[str]]
"""

# Optimal Solution
    # Keyword:  "find all possibility" -> Backtracking 
    # Approach: Define a DFS function to build string, keep track of number of bracket. explore every combination by making a binary choice ( include '(' or ')') for each element
        # Always open '(' if left > 0; only close ')' if left < right to maintain validity.
    # Tricks - DFS
        # 1.Draw a decision tree to help us understand recursive problem
        # 2.Procedure: base case -> current level -> next level
     # Tricks - Bracket Matching
        # 1. Base case: when left == 0 and right == 0, we found a valid combo.
        # 2. Valid condition: 'left' tracks remaining (, 'right' tracks remaining ). 
        # 3. If neither '(' nor ')' can be placed, it's a dead end. Backtrack.

from typing import List
class Solution:
    def generateParaenthesis(self, n:int) -> List[str]:
        res = []

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left,right,subset):
            if left == 0 and right ==0:
                # Convert the list of characters back to a single string
                res.append("".join(subset))
                return
            # current level - pick '('
            if left > 0:
                subset.append('(')
                # next level
                dfs(left-1,right,subset)
                # current level - don't pick (Backtrack)-> no next level
                subset.pop()
            # current level - pick ')'
            # condition: left < right means there are unmatched '(' waiting for pairs
            if left < right: #  剩餘的左括號少於右括號，代表前面已經放了比較多左括號
                subset.append(')')
                # next level
                dfs(left,right-1,subset)
                # current level - don't pick (Backtrack)-> no next level 
                subset.pop()
        dfs(n, n, [])
        return res

# Time complexity: O(4^N / sqrt(N)) ... bounded by the N-th Catalan number.
  # number of nodes: if no constraints, its 2^(2N) -> 4^N, the total number of bracket is 2N, and every position you have 2 choice
  # copying each subset takes O(N) time
# Space Complexity: O(N) ...we need store N dfs recursion stack as height

def test():
    sol = Solution()
    n = 3
    result = sol.generateParenthesis(n)
    print(f"Result: {result}") 
    # Expected: ["((()))","(()())","(())()","()(())","()()()"]

if __name__ == "__main__":
    test()



