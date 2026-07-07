"""
 OOD: No
 Constraints: No
 input : String, String
 output : bool
"""
# Brute Force: 
    # Traverse all substrings of s2 that have the exact same length as s1, sort both the substring and s1, and check if they match. -> : O( (n2-n1) * N1logO(1))
    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1),len(s2)
        if n1 > n2:
            return False
        sorted_s1 = sorted(s1)

        for i in range(n2-n1+1):
            substring = s2[i:i+n1]
            if sorted(substring) ==sorted_s1:
                return True
        return False

# Optimal Solution
    # Goal: Save time complexity 
    # Keyword:  “Permutation”, “Anagram”, “Subarrays of length K"  -> Sliding Window (Fixed Size) -edge case
    # Approach:  Maintain a sliding window of fixed length len(s1) across s2 , use frequency map to count character as the window moves , Check if the current window matches s1's frequency 
    # Tricks
        #  Since we are dealing with count the same anagram , can build count array with 26 alphabet O(1). No need for hashMapO(N).
        #  Fix size sliding window need to remember to Final check for the last window.
    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2 or not n1:
            return False
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        for i in range(len(s1)):
            s1_counts[ord(s1[i])-ord('a')] +=1
            s2_counts[ord(s2[i])-ord('a')] +=1
        if s1_counts == s2_counts:
            return True

        # Slide the window across s2
        for i in range(n1,n2):
            # Add the incoming character to the window
            s2_counts[ord(s2[i])-ord('a')] +=1
            # Remove the outgoing character from the window
            s2_counts[ord(s2[i-n1]) - ord('a')] -= 1
            if s1_counts ==s2_counts:
                return True
        return False
# Time complexity: O(N2) ...traverse size N2 array, N2 is the length of s2
# Space complexity:  O(1)...create size 26 Map array. 

def test():
    sol = Solution()
    result = sol.checkInclusion("abc","lecabee")
    print(f"Result: {result}")
if __name__ == "__main__":
    test()



