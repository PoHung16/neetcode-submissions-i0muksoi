class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 題型Keyword:  “substring” -> Sliding Window (Variable Size)
        # 腦中圖像: A window that expands until it meets a condition, then shrinks from the left.
        # 動作記憶法 - 3個步驟 
        #ps. Edge case
        if not t or not s: return ""
        # ps. If there are 2 input String to match -> need 2 state map
        # Step1: Initialize start pointer, result,  a frequency map store window's info, and target map to store target's info
        start = 0
        res_range, res_len = [-1, -1], float("inf")

        target_map = {}
        for char in t:
            target_map[char] = target_map.get(char, 0) + 1
        window_map = {}
        # 'need' is the number of unique characters in t that must be satisfied.
        # 'have' is how many unique characters currently meet the requirement.
        have, need = 0, len(target_map)

    
        # Step2:  Expand Phase - Traverse the array with the 'end' pointer.
        for end in range(len(s)):
            # Step 2-1: Update the State (Add the incoming character)
            window_map[s[end]] = window_map.get(s[end], 0) + 1
            if s[end] in target_map and window_map[s[end]] == target_map[s[end]]:
                have += 1
            # Step 2-2: Shrink Phase - While the "have==need" condition is meet. we must Update the State and shrink from the left.
            while have == need:
                # Update result if this window is smaller than the previous minimum, means we find the shorter minimum substring
                if (end - start + 1) < res_len:
                    res_range = [start, end]
                    res_len = end - start + 1
                left_char = s[start]
                window_map[left_char] -= 1

                # If removing this char makes the window invalid
                if left_char in target_map and window_map[left_char] < target_map[left_char]:
                    have -= 1
                
                start += 1

               
        # Step 3: Step 3: 回傳結果
        start, end = res_range
        return s[start : end + 1] if res_len != float("inf") else ""

# Time Complexity: O(N + K) - travesr size N array, and size K array
# Space Complexity: O(M) - M is the number of unique characters in s and t.
def test():
    sol = Solution()
    result = sol.minWindow("OUZODYXAZV","XYZ")
    print(f"Result: {result}")
test()

