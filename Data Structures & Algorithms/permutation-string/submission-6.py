"""
 OOD: No
 Constraints: No
 input : String, String
 output : bool
"""
# Keyword: “Permutation”, “Anagram”, “Subarrays of length K"  -> Sliding Window (Fixed Size)
# Image: Slide an Fix s1-sized window across s2; check for matching character counts at each step.
# Tricks:
    #  Since we are dealing with count the same anagram , can build count array with 26 alphabet O(1). No need for hashMapO(N).
    #  Fix size sliding window need to remember to Final check for the last window.
    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2 or not n1 :
            return False
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        for i in range(len(s1)):
            s1_counts[ord(s1[i])-ord('a')] +=1
            s2_counts[ord(s2[i])- ord('a')] +=1
        for i in range(n1,n2):
            # 1. Every step Check if the current window is a perfect match.
            if s1_counts == s2_counts:
                return True
            #  2. Slide the window one step to the right:
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i - n1]) - ord('a')] -= 1

        return s1_counts == s2_counts #Final check for the last window.

# Time complexity: O(N2) ...traverse size N2 array, N2 is the length of s2
# Space complexity:  O(1)...create size 26 Map array. 

def test():
    sol = Solution()
    result = sol.checkInclusion("abc","lecabee")
    print(f"Result: {result}")
if __name__ == "__main__":
    test()



