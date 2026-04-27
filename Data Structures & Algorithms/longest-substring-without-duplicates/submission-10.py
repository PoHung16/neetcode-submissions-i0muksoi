"""
 OOD: No
 Constraints: No
 input : String
 output : int
"""
# Keyword : “A Consecutive sequence”, "Substring"  -> Sliding Window (Variable Size) - edge case
# Image :  A state window that expands until it meets a condition, then shrinks from the left, usually implement with statemap.

class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        if not s:
            return 0
        state = {} 
        start = 0
        res = 0
        for end in range(len(s)):
            state[s[end]] = state.get(s[end],0) + 1
            while state[s[end]] > 1:
                state[s[start]] -= 1
                start+=1
            res= max(res,end-start+1)
        return res
            
def test():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("zxyzxyz")
    print(f"Result: {result}")
if __name__ == "__main__":
    test()

# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(M)...create size M Map. m is the total number of unique characters
