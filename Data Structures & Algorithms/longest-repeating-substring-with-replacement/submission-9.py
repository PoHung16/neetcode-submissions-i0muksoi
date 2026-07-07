"""
 OOD: No
 Constraints: No
 input : String , int
 output : int
"""
# Brute Force: 
    # Use two nested loops to generate all possible substrings , find the frequency of the most frequent character in each,  calculating the changes needed to turn it uniform ->O(N^3)

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                substring = s[i:j]
                # Count frequencies of characters in the substring
                counts = {}
                for char in substring:
                    counts[char] = counts.get(char, 0) + 1
                most_frequent = max(counts.values()) if counts else 0
                # Characters to replace = total length - most frequent character count
                if len(substring - most_frequent)<=k:
                    max_len = max(max_len, len(substring))
        return max_len

# Optimal Solution
    # Goal: Save time complexity from O(N^3) -> O(N)
    # Keyword:  "Longest Substring or Longest Repeating character"  -> Sliding Window (Variable Size) -edge case
    # Approach:  A state map window that expands until it meets a condition, then shrinks from the left
    # Tricks
        # Longest Repeating Character Replacement : while end - start + 1 - max_frequency > k

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # edge case
        if not s:
            return 0
        stateMap = {}
        start = 0
        max_frequency = 0
        max_length = 0
        for end in range(len(s)):
            stateMap[s[end]] = stateMap.get(s[end],0)+1
            max_frequency = max(max_frequency,stateMap[s[end]])
            while end-start+1 - max_frequency > k:
                stateMap[s[start]]-=1
                start+=1
            max_length = max(max_length,end-start+1)
        return max_length
#  Time complexity: O(N) ...traverse size N array
# Space complexity:  O(M)...create size M Map. m is the total number of unique characters

def test():
    sol = Solution()
    result = sol.characterReplacement("XYYX",2)
    print(f"Result: {result}")
if __name__ == "__main__":
    test()

