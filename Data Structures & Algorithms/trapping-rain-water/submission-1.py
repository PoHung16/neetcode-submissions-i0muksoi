class Solution:
    def trap(self, height: List[int]) -> int:
        # 題型Keyword: “Palindrome” , “Sorted Array”, “Remove duplicates”, “Target Sum <=2”, “maximum area of water” -> Two pointer Basic
        # 腦中圖像: two opposite pointers closing in.
        # 動作記憶法 - 3個步驟 
        #核心邏輯：
        #1.想像你現在要計算一個山谷能裝多少水。水要留住，一定要有左右兩面牆。
        #A.短板效應：一個山谷能裝多少水，取決於最短的那塊木板。
        #B.為什麼讓「矮的那邊」pointer動？ 假設左邊5米，右邊10米。我們不需要知道右邊中間還有什麼，我們只知道右邊已經有一面 10 米高的牆在那裡守著了
        #對左邊這格的坑來說，能限制它裝水量的「短板」一定是左邊這面 5 米的牆。
       
        # Step1: Initialize pointers at both ends of the array + leftMax, RightMax
        l = 0
        r = len(height) -1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        #Step2:  Traverse the array: while left< right
        while l < r:
            # Step 2-1 : Check the current state and shift pointers and upfate leftMax, rightMax , result
            if leftMax < rightMax:
                l = l + 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l] # 計算當前這一格能接多少水
            else:
                r = r - 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r] # 計算當前這一格能接多少水
        # Step3 : Return the result 
        return res

# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable
def test():
    sol = Solution()
    result = sol.trap([1,7,2,5,4,7,3,6])
    print(f"Result: {result})")
test()



        