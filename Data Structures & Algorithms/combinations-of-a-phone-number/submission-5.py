"""
 OOD: No
 Constraints: n<=20 -> Backtracking
 input : str
 output : List[str]
"""
# Optimal Solution
    # Keyword:  "find all possibility" -> Backtracking 
    # Approach:  Define a DFS function to .  At each level, loop through  all mapped letters for digits[i], pick it and move to the next position.
    # Tricks - DFS
        # 1.Draw a decision tree to help us understand recursive problem
        # 2.Procedure: base case -> current level -> next level
    # Tricks - Phone Mapping
        # 1. Edge case: empty input 'digits' -> return [] directly.
        # 2. Base case: when index i == len(digits), we formed a valid combination -> join and append to res.
        # ps. Map each digit to its corresponding letters.
      

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: empty input string
        if not digits:
            return [] 
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        
        def dfs(i, subset):
            # base case: processed all digits
            if i == len(digits):
                res.append("".join(subset))
                return
                
            # current level - get letters corresponding to the current digit
            letters = digit_map[digits[i]]
            
            # traverse all mapped letters for digits[i]
            for char in letters:
                # current level - pick
                subset.append(char)
                # next level - process next digit
                dfs(i + 1, subset)
                # current level - don't pick (Backtrack)
                subset.pop()
                #因為在 for 迴圈裡面，「切換到下一個選項」這件事已經被 for 迴圈自動處理掉了！
                
        dfs(0, [])
        return res

# Time complexity: O(4^N * N)
  # In the worst case (digits '7' or '9'), each digit maps to 4 letters, giving 4^N combinations.
  # Converting each subset of length N into a string takes O(N) time.
# Space Complexity: O(N) ... store N recursion call


def test():
    sol = Solution()
    digits = "23"
    result = sol.letterCombinations(digits)
    print(f"Result: {result}") 
    # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

if __name__ == "__main__":
    test()











class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Step 1: initialize the final result to store our subsets
        #Step1-1 Edge case check - crucial for this specific problem
        #If the input digits is an empty string "", your dfs(0, []) will run, and append an empty string "" to your res, but we are expecting it return []
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        #Step 2: define dfs function : def dfs(i, subset)
        def dfs(i, subset):
            #Step2-1: Base case : when to stop and what should we do
            if len(subset) == len(digits):
                res.append("".join(subset))
                return
            #Step2-2: Constraints : None
            #Step2-3: Choices with Backtracking : include every character in the Map
            for c in digitToChar[digits[i]]:
                subset.append(c)
                dfs(i + 1, subset)
                subset.pop()

        #Step 3: call dfs function and return result
        dfs(0, [])

        return res