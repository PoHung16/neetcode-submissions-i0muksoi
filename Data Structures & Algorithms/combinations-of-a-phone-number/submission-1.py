class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Step 1: initialize the final result to store our subsets
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        #Step 2: define dfs function : def dfs(i,curStr)
        def dfs(i, curStr):
            #Step2-1: Base case : when to stop and what should we do
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            #Step2-2: Constraints : None
            #Step2-3: Choices with Backtracking : include every character in the Map
            for c in digitToChar[digits[i]]:
                dfs(i + 1, curStr + c)
        #Step 3: call dfs function and return result
        if digits:
            dfs(0, "")

        return res