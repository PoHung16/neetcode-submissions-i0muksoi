"""
 OOD: No
 Constraints: n <= 20 -> Backtracking
 input : str
 output : List[List[str]]
"""
# Optimal Solution
    # Keyword:  "find all possibility" -> Backtracking
    # Approach: Define a DFS function to explore every potential partition point.  At each level, check all substrings s[i:j+1].  If it is a palindrome, pick it and explore the remaining string.    
    # Tricks - DFS
        # 1.Draw a decision tree to help us understand recursive problem
        # 2.Procedure: base case -> current level -> next level
    # Tricks - Partitioning & Palindrome
        # 1. Base case: when index i == len(s), we reached the end of string -> found a valid partition.
        # 2. Decision logic: slice substring s[i:j+1]. Only call dfs(j + 1) if s[i:j+1] == s[i:j+1][::-1].

from typing import List

class Solution:
    def partition(self, s:str) -> List[List[str]]:
        res = []
        def is_palindrome(sub):
            return sub == sub[::-1]
        def dfs(i,subset):
            # base case: processed the whole string
            if i == len(s):
                res.append(subset.copy())
                return
            # explore every possible ending position 'j' starting from 'i'
            for j in range(i, len(s)):
                sub = s[i : j+1]
                # only proceed if current substring is a palindrome
                if is_palindrome(sub):
                    # current level - pick
                    subset.append(sub)
                    # next level - process remaining string starting from j + 1
                    dfs(j+1,subset)
                    # current level - don't pick (Backtrack) -> no next level
                    subset.pop()
        dfs(0,[])
        return res

# Time complexity: O(N * 2^N)
  # There are 2^(N-1) possible partition ways (placing cuts between characters). 每個間隔要切or不切
  # Checking palindrome and copying the subset take up to O(N) time at each step.
# Space Complexity: O(N) ... store N recursion stack

def test():
    sol = Solution()
    s = "aab"
    result = sol.partition(s)
    print(f"Result: {result}") 
    # Expected: [["a","a","b"],["aa","b"]]

if __name__ == "__main__":
    test()


