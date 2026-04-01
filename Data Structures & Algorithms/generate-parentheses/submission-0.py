class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing parenthesis if closed < n and closing parenthesis < open parenthesis
        # valid if  open == closed == n

        # Step 1: initialize the final result to store our subsets(stacks)
        stack = []
        res = []
        # Step 2: define dfs function : def dfs(openN, closedN)
        def dfs(openN, closedN):
            #Step2-1: Base case : when to stop and what should we do
            if openN == closedN == n:
                res.append("".join(stack))
                return
            #Step2-2: Decision Tree Start : include or not include with條件
            if openN < n:
                #include
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                #include
                stack.append(")")
                dfs(openN, closedN + 1)
                #彈回來
                stack.pop()

        dfs(0, 0)
        return res