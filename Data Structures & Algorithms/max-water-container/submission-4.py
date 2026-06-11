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
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r= 0, len(heights)-1
        max_area = 0
        while l < r:
            width = r - l
            height = min(heights[l],heights[r])
            area = height * width
            max_area = max(area,max_area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return max_area


def test():
    sol = Solution()
    result = sol.maxArea([1,7,2,5,4,7,3,6])
    print(f"Result: {result})")
if __name__ == "__main__":
    test()
# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable




