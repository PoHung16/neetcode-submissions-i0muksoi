"""
 OOD: No
 Constraints: No
 input : str
 output : boolean
"""
# Keyword : “Palindrome", "Duplicate", "Frequency count", "Matching pairs", "Anagrams"  -> Basic Two pointer 
# Image : Two pointer Shrink from both ends to find the perfect fit

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l<r and not self.alphaNum(s[l]):
                l += 1
            while l<r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

def test():
    sol = Solution()
    result = sol.isPalindrome("Was it a car or a cat I saw?")
    print(f"Result: {result})")

if __name__ == "__main__":
    test()


# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable