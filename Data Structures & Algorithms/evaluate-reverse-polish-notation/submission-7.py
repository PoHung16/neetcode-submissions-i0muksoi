"""
 OOD: No
 Constraints: No
 input : List[String]
 output : integer
"""

# Optimal Solution
    # Keyword : “Parentheses","Reverse Polish Notation" -> Basic Stack
    # Approach : Map the pairs. Traverse the string: push "integet" brackets into stack, and pop "integer" twice to calcuate,and push the result back.

from typing import List
class Solution:
    def evalRPN(self,tokens:List[str])->str:
        operation ={
            "+" : lambda a,b : a+b,
            "-" : lambda a,b : a-b,
            "*" : lambda a,b : a*b,
            "/" : lambda a,b : int(a/b),
        }
        stack = []
        for token in tokens:
            if token not in operation:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = operation[token](a,b)
                stack.append(result)
        return stack[-1] #stack[0]也可以

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & Size 4 Map


def test():
    sol = Solution()
    tokens = ["1","2","+","3","*","4","-"]
    result = sol.evalRPN(tokens)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


