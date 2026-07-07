"""
 OOD: No
 Constraints: No
 input : String
 output : boolean
"""
# Optimal Solution
    # Keyword : “Parentheses","Reverse Polish Notation" -> Basic Stack
    # Approach : Map the pairs. Traverse the string: push left brackets into stack, and pop on  right brackets if match.
    # Tricks
        # Match the stacks : if stack and stack[-1] == closeToOpen[char]
class Solution:
    def isValid(self,s:str)->bool:
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        stack = []
        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) ==0 # means every left have a match
            

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & Size 3 Map

def test():
    sol = Solution()
    nums = s = "[]"
    result = sol.isValid(s)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


