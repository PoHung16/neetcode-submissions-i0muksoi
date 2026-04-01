class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < n and closing parenthesis < open parenthesis
        # valid if  open == closed == n

        # Step 1: initialize the final result to store our subsets(stacks)
        res = []
        # Step 2: define dfs function : def dfs(openN, closedN)
        def dfs(openN, closedN,subset):
            # Step2-1: Base case : when to stop and what should we do
            if openN == closedN == n:
                res.append("".join(subset))
                return
            # Step2-2: Constraints :  
            # openN < n
            # closedN < openN
            if openN < n:
                #Step2-3:  Choices with Backtracking  : include openN / closedN
                #include
                subset.append("(")
                dfs(openN + 1, closedN,subset)
                subset.pop()
            if closedN < openN:
                #Step2-3:  Choices with Backtracking  : include openN / closedN
                #include
                subset.append(")")
                dfs(openN, closedN + 1, subset)
                #彈回來
                subset.pop()

        dfs(0, 0,[])
        return res