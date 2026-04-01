class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        # 題型Keyword:  題目提到「連續子陣列」-> Sliding Window (Variable Size)
        # 腦內圖像：A window that expands until it meets a condition, then shrinks from the left.
        # 動作記憶法 - 3個步驟 
        #Step1: Initialize start pointer, result, and a state map to store window's info
        start  = 0
        res = 0
        state = {} # {val: count}
        
        #Step2:  Expand Phase - Traverse the array with the 'end' pointer.
        for end in range(len(s)):
            # Step 2-1: Update the State (Add the incoming character).
            state[s[end]] = state.get(s[end],0) + 1
            # Step 2-2: Shrink Phase - While the "No Duplicates" condition is violated. we must Update the State and shrink from the left.
            while state[s[end]] > 1:
                state[s[start]] -= 1
                start+=1
            # 2-3: Update Result - The window [start, end] is now "Valid".
            res= max(res,end-start+1)
           
        #Step 3: return the result
        return res
# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(M)...create size M Map. m is the total number of unique characters
def test():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("zxyzxyz")
    print(f"Result: {result}")
test()

