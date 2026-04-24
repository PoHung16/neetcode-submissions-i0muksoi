"""
 OOD: No
 Constraints: No
 input : str
 output : str
"""

# Keyword : “Longest Palindromic Substring” -> Two pointer close out
# Image :  Pick a center, then push outward with 2 pointer for both odd and even lengths.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0   
        def expand(l, r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # when we stop, l and r both already proceed once extra，so we return s[l+1 : r]
        for i in range(len(s)):
            # Odd center expand (e.g., "aba"), l and r start with same position
            s1 = expand(i,i)
            # Even center expand (e.g., "abba"), l and r start with adjacent position
            s2 = expand(i,i+1)
            if len(s1)>res_len:
                res = s1
                res_len = len(s1)
            if len(s2)>res_len:
                res = s2
                res_len = len(s2)
        return res

def test():
    sol = Solution()
    result = sol.longestPalindrome("ababd")
    print(f"Result: {result})")
test()
# Time complexity: O(N^2) 
    # traverse size N array to pick  all possible center to expand :O(N)
    # every center need to expand : O(N)
# Space complexity:  O(N)....create size N result

