"""
 OOD: No
 Constraints: No
 input : String
 output : boolean
"""
# Keyword : “Parentheses","Reverse Polish Notation" -> Basic Stack
# Image : Map the pairs, then traverse the string: push the lefts, and for every right, pop the top if stack is not empty and stack top is a match
class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        stack = []
        for char in s:
            if char not in closeToOpen:
                stack.append(char)
            else:
                if stack and stack[-1]==closeToOpen[char]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0


def test():
    sol = Solution()
    nums = s = "[]"
    result = sol.isValid(s)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & Size 3 Map
