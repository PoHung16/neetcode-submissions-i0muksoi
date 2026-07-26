"""
 OOD: No
 Constraints: No
 input : List[String]
 output : integer
"""
# Optimal Solution
    # Keyword:  "Valid Parentheses" or "Reverse Polish Notation"  -> Stack (LIFO) 
    # Approach: 
        # 1. Use a HashMap to store matching close-to-open bracket pairs.
        # 2. Use a Stack to track open bracket
        # 3. Traverse the array :
            # push open brackets onto the stack
            # Operation:
                # no need condition -> pop from the stack
                # if stack and check the top stack is a match -> pop from the stack
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str])->int:
        closeToOpen ={
            "+" : lambda a,b : a+b,
            "-" : lambda a,b : a-b,
            "*" : lambda a,b : a*b,
            "/" : lambda a,b : int(a/b)
        }
        stack = []
        for token in tokens:
            if token not in closeToOpen:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = closeToOpen[token](a,b)
                stack.append(result)
        return stack[-1]


# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & Size 4 Map


def test():
    sol = Solution()
    tokens = ["1","2","+","3","*","4","-"]
    result = sol.evalRPN(tokens)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


