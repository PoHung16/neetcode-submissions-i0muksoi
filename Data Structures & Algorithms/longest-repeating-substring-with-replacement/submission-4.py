class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 題型Keyword:  題目提到「連續子陣列」-> Sliding Window (Variable Size)
        # 腦內圖像：A window that expands until it meets a condition, then shrinks from the left.
        # 動作記憶法 - 3個步驟 
        # Step1: Initialize start pointer, result, max frequency, and a frequency map store window's info
        state = {}
        start = 0
        res = 0
        max_frequency = 0 

       #Step2:  Expand Phase - Traverse the array with the 'end' pointer.
        for end in range(len(s)):
            # Step 2-1: Update the State (Add the incoming character) and max frequency
            state[s[end]] = state.get(s[end],0) + 1
            max_frequency = max(max_frequency, state[s[end]])
            # Step 2-2: Shrink Phase - While the "Window length -max_frequency >k" condition is violated. we must Update the State and shrink from the left.
            while (end - start + 1) - max_frequency > k:
                state[s[start]] -= 1
                start += 1
            # 2-3: Update Result - The window [start, end] is now "Valid".
            res = max(res, end - start + 1)
        #Step 3: 回傳結果
        return res
# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(M)...create size M Map. m is the total number of unique characters
def test():
    sol = Solution()
    result = sol.characterReplacement("XYYX",2)
    print(f"Result: {result}")
test()


