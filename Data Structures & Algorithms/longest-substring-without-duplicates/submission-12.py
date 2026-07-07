"""
 OOD: No
 Constraints: No
 input : String
 output : int
"""
# Brute Force: 
    # Use two nested loops to generate all possible substrings and a helper function with a set to check if each substring contains only unique characters, keeping track of the maximum length found. -> O(N^2)
class Solution:
    def lengthOfLongestSubstring(self, string:str) -> int:
        def is_unique(sub_str:str)->bool:
            return len(set(sub_str)) == len(sub_str)
        max_len = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if is_unique(string[i:j]):
                    max_len = max(max_len, j-i)
        return max_len

# Optimal Solution
    # Goal: Save time complexity from O(N^2) -> O(N)
    # Keyword:  "Longest Substring or Longest Repeating character"  -> Sliding Window (Variable Size) -edge case
    # Approach:  A state map window that expands until it meets a condition, then shrinks from the left
class Solution:
    def lengthOfLongestSubstring(self, string:str) -> int:
        hashMap = {}
        start = 0
        max_len = 0
        for end in range(len(string)):
            hashMap[string[end]] = hashMap.get(string[end],0)+1
            while hashMap[string[end]]>1:
                hashMap[string[start]] -= 1
                start += 1
            max_len = max(max_len,end-start+1)
        return max_len

# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(M)...create size M Map. m is the total number of unique characters
                   
            
def test():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("zxyzxyz")
    print(f"Result: {result}")
if __name__ == "__main__":
    test()
