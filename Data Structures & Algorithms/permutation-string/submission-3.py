class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 題型Keyword: "Permutation as a substring" -> Sliding Window (Fixed Size)
        # 腦中圖像: A fixed-size window of length len(s1) sliding across s2.
        # 動作記憶法 - 3個步驟 

        #ps. Edge case
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2 or not n1:
            return False

        # Step 1: Initialize frequency maps array for s1 and the first window of s2.
        s1_counts = [0] * 26
        window_counts = [0] * 26
        for i in range(len(s1)):
            s1_counts[ord(s1[i])- ord('a')] += 1
            window_counts[ord(s2[i])- ord('a')] += 1
        
        
        # Step 2: Expand phase: Traverse the array with the i pointer.
        for i in range(n1,n2):
            # Step 2-0: Every time Check if the current window is a permutation (Match!).
            if s1_counts == window_counts:
                return True
            # Step 2-1: Update the State (Add the incoming character) 
            window_counts[ord(s2[i]) - ord('a')] += 1
            # Step 2-2: Shrink Phase  - while the window surpass fixed sized, we must Update the State and shrink from the left.
            window_counts[ord(s2[i - n1]) - ord('a')] -= 1

        # Step 3: Return result: Final check for the last window.
        return s1_counts == window_counts
# Time complexity: O(N2) ...traverse size N2 array
# Space complexity:  O(1)...create size 26 Map array. 
def test():
    sol = Solution()
    result = sol.checkInclusion("abc","lecabee")
    print(f"Result: {result}")
test()
