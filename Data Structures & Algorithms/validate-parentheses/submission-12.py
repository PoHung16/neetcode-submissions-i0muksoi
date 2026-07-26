"""
 OOD: No
 Constraints: No
 input : String
 output : boolean
"""
# Optimal Solution
    # Keyword:  "Valid Parentheses" or "Reverse Polish Notation"  -> Stack (LIFO) 
    # Approach: 
        # 1. Use a HashMap to store matching close-to-open bracket pairs.
        # 2. Use a Stack to track open bracket
        # 3. Traverse the array :
            # push open brackets onto the stack
            # if stack and check the top stack is a match -> pop from the stack
class Solution:
    def isValid(self, s:str) -> bool:
        closeToOpen = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        stack = []
        for i in range(len(s)):
            if s[i] not in closeToOpen:
                stack.append(s[i])
            else:
                if stack and stack[-1] == closeToOpen[s[i]]:
                    stack.pop()
                else:
                    return False

                
        return len(stack)==0

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Stack  & Size 3 Map

def test():
    sol = Solution()
    nums = s = "[]"
    result = sol.isValid(s)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


