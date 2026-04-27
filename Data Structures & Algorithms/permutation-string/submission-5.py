"""
 OOD: No
 Constraints: No
 input : String, String
 output : int
"""
# Keyword: “Permutation”, “Anagram”, “Subarrays of length K"  -> Sliding Window (Fixed Size)
# Image: A state window of a constant width that slides from left to right. When a new element enters from the right, shrink from the left ,  usually implemented with a statemap.
# Tricks:
    # if you need to count the same anagram , can build count array with 26 alphabet
    # Two map, if there are 2 input String to match

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #ps. Edge case
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2 or not n1:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26
        for i in range(len(s1)):
            s1_counts[ord(s1[i])- ord('a')] += 1
            s2_counts[ord(s2[i])- ord('a')] += 1
        
        for i in range(n1,n2):
            #  Every time Check if the current window is a permutation (Match!).
            if s1_counts == s2_counts:
                return True
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i - n1]) - ord('a')] -= 1

        return s1_counts == s2_counts #Final check for the last window.

def test():
    sol = Solution()
    result = sol.checkInclusion("abc","lecabee")
    print(f"Result: {result}")
if __name__ == "__main__":
    test()


# Time complexity: O(N2) ...traverse size N2 array, N2 is the length of s2
# Space complexity:  O(1)...create size 26 Map array. 
