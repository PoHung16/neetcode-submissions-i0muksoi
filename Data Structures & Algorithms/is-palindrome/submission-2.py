class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 題型Keyword: “Palindrome” , “Sorted Array”, “Remove duplicates”, “Target Sum <=2”, “maximum area of water” -> Standard Two pointer 
        # 腦中圖像: Two opposite pointers closing in
        # 動作記憶法 - 3個步驟 
        # Step1:  Initialize pointers at both ends of the array.
        l, r = 0, len(s) - 1
        # Step2: Traverse the array : while left< right
        while l < r:
            #Step 2-1: Check the current state and shift pointers
            while l<r and not self.alphaNum(s[l]):
                l += 1
            while l<r and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        # Step3 : Return the result 
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable
def test():
    sol = Solution()
    result = sol.isPalindrome("Was it a car or a cat I saw?")
    print(f"Result: {result})")
test()
    