class Solution:
    def longestPalindrome(self, s: str) -> str:
       # 題型Keyword: Longest Palindromic Substring ->  2 pointer closing out
        #腦中圖像: expand all possible center to find longest Palindrome with 2 pointer closing out
        #動作記憶法 - 三個步驟 
        res = ""
        res_len = 0   
        # Step 1 : Expand the center to the longest Palindrome by 2 opposite pointer
        def expand(l, r):
            while l>=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]  # when we stop, l and r both already proceed once extra，so we return s[l+1 : r]

        # Step 2: Traverse the array for all possible center to expand
        for i in range(len(s)):
            # Step 2-1: Odd center expand (e.g., "aba"), l and r start with same position
            s1 = expand(i,i)
            # Step 2-2: Even center expand (e.g., "abba"), l and r start with adjacent position
            s2 = expand(i,i+1)
            # Step 2-3: update the result and result len
            if len(s1)>res_len:
                res = s1
                res_len = len(s1)
            if len(s2)>res_len:
                res = s2
                res_len = len(s2)
        #Step 3: 回傳結果
        return res


# Time complexity: O(N^2) ...traverse nested loop N array for expand and for all possible center to expand
# Space complexity:  O(N)....create size N result
def test():
    sol = Solution()
    result = sol.longestPalindrome("ababd")
    print(f"Result: {result})")
test()
    

