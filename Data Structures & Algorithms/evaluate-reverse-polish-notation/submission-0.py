"""
 OOD: No
 Constraints: No
 input : List[String]
 output : integer
"""
# Keyword : “Parentheses","Reverse Polish Notation" -> Basic Stack
# Image : Map the pairs, then traverse the string: push the lefts, and for every right, pop the top to if stack is not empty and stack top is a match
# Image : Map the Opearation, then traverse the string: push the numbers, and for every operator, pop two, calculate, and push the result back."


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        # 使用 dictionary 簡化運算邏輯
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)  # 注意：題目要求向零取整
        }
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                # 1. 遇到符號，取出最後兩個數字
                b = stack.pop()
                a = stack.pop()
                # 2. 計算後推回 Stack
                stack.append(operators[token](a, b))                
                
        return stack[0]

def test():
    sol = Solution()
    tokens = ["1","2","+","3","*","4","-"]
    result = sol.evalRPN(tokens)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & Size 4 Map


