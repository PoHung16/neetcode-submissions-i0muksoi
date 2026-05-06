"""
 OOD: No
 Constraints: No
 input : List[String]
 output : integer
"""
# Keyword : “Parentheses","Reverse Polish Notation" -> Basic Stack
# Image : Map the pairs, then traverse the string: push the lefts, and for every right, pop the top to if stack is not empty and stack top is a match
# Image : Map the Operation, then traverse the string: push the numbers, and for every operator, pop two, calculate, and push the result back."


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            '+' : lambda a,b: a+b,
            '-' : lambda a,b: a-b,
            '*' : lambda a,b: a*b,
            '/' : lambda a,b: int(a/b) #Assume that division between integers always truncates toward zero.
        }
        stack = []
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = operations[token](a,b)
                stack.append(result)
        return stack[0] #stack[-1]也可以
    
def test():
    sol = Solution()
    tokens = ["1","2","+","3","*","4","-"]
    result = sol.evalRPN(tokens)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & Size 4 Map


