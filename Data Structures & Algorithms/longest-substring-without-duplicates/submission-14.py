"""
 OOD: No
 Constraints: No
 input : String
 output : int
"""
# Brute Force: 
    # String - Use two nested loops to generate all possible substrings and a helper function with a set to check if each substring contains only unique characters, keeping track of the maximum length found. -> O(N^3)
class Solution:
    def lengthOfLongestSubstring(self, string:str) -> int:
        def is_unique(sub_str:str)->bool:
            return len(set(sub_str)) == len(sub_str)
        max_len = 0
        for i in range(len(string)):
            for j in range(i+1,len(string)+1):
                substring = string[i:j]
                if is_unique(substring): #O(N)
                    max_len = max(max_len,len(substring))
        return max_len

# Optimal Solution
    # Goal:  O(N^2) -> O(N)
    # Keyword:  "Longest Substring or Longest Repeating character"  -> Sliding Window (Variable Size) -edge case
    # Approach: 
        # 1. Use two pointers (start and end) and a state variable map to record window state
        # 2. Expand from the right, and once condition happen ( while state[s[end]] > 1 )
        # 3. update the global variable & state variable & window size,  then  shrink the window from the left
# Jump to Minimum Size Subarray Sum

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        start = 0
        hashMap = {}
        max_length = 0
        for end in range(len(s)):
            hashMap[s[end]] = hashMap.get(s[end],0) + 1
            while hashMap[s[end]] > 1:
                hashMap[s[start]] -= 1
                start+=1
            max_length = max(max_length, end - start +1 )# global variable need to be update outsdie the condition in this case
        return max_length

# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(M)...create size M Map. m is the total number of unique characters
                   
def test():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("zxyzxyz")
    print(f"Result: {result}")
if __name__ == "__main__":
    test()
