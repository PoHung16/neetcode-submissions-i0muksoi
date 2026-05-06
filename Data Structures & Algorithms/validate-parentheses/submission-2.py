"""
 OOD: No
 Constraints: No
 input : String
 output : boolean
"""
# Keyword : “ “Parentheses" or "brackets" -> Basic Stack
# Image : Map the pairs, then traverse the string: push the lefts, and for every right, pop the top to if stack is not empty and stack top is a match
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{',']':'['}
        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

def test():
    sol = Solution()
    nums = s = "[]"
    result = sol.isValid(s)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & Size 3 Map
