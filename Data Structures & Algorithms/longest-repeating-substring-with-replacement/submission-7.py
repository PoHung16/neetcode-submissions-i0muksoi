"""
 OOD: No
 Constraints: No
 input : String , int
 output : int
"""
# Keyword : “A Consecutive sequence”, "Substring"  -> Sliding Window (Variable Size) - edge case
# Image :  A state window that expands until it meets a condition, then shrinks from the left, usually implement with statemap.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        state = {}
        start = 0
        res = 0
        max_frequency = 0
        for end in range(len(s)):
            state[s[end]] = state.get(s[end],0) + 1
            max_frequency = max(max_frequency, state[s[end]])
            while (end - start + 1) - max_frequency > k:
                state[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        return res

def test():
    sol = Solution()
    result = sol.characterReplacement("XYYX",2)
    print(f"Result: {result}")
if __name__ == "__main__":
    test()
# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(M)...create size M Map. m is the total number of unique characters

