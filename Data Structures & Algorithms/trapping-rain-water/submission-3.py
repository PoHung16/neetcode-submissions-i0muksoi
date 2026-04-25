"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Keyword : “Palindrome", "Target Sum", “maximum area of water”  -> Basic Two pointer 
# Image : Two pointer Shrink from both ends to find the perfect fit
# Tricks:
   # When you're solving the water volume problem, always move the shorter pointer. It’s the only way to potentially find a higher bottleneck and increase the area
   # 如果你移動長的那一邊，矩形的高度只會被原本那個「短邊」卡死，或者變得更短。高度沒變、寬度變小，面積絕對縮水。


class Solution:
    def trap(self, height: List[int]) -> int: 
        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l < r: 
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax,height[l])
                res += leftMax - height[l]  # 計算當前這一格能接多少水
            else:
                r-=1
                rightMax = max(rightMax,height[r])
                res+= rightMax-height[r]
        return res

def test():
    sol = Solution()
    result = sol.trap([1,7,2,5,4,7,3,6])
    print(f"Result: {result})")
if __name__ == "__main__":
    test()

# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable

        