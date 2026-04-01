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