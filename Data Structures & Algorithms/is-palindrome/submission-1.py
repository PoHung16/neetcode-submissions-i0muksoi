class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Step1:  初始化左、右指針
        l, r = 0, len(s) - 1
        #Step2:  while left< right
        while l < r:
            #Step 2-1: 檢查目前的狀態 : 處理非字母/數字 (跳過)
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            #Step 2-1: 檢查目前的狀態 :是否相等
            if s[l].lower() != s[r].lower():
                return False

            #Step 2-2: 決定移動哪一個指針 (這是最關鍵的一步！)
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))