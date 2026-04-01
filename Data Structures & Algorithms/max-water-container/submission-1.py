class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 題型Keyword: “Palindrome” , “Sorted Array”, “Remove duplicates”, “Target Sum <=2”, “maximum area of water” -> Two pointer Basic
        # 腦中圖像: two opposite pointers closing in.
        # 動作記憶法 - 3個步驟 
        # Step1:  Initialize pointers at both ends of the array.
        l, r = 0, len(height) - 1
        res = 0
        #Step2:  Traverse the array: while left< right
        while l < r:
            # Step 2-1 : Check the current state and shift pointers
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        # Step3 : Return the result 
        return res
# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable
def test():
    sol = Solution()
    result = sol.maxArea([1,7,2,5,4,7,3,6])
    print(f"Result: {result})")
test()