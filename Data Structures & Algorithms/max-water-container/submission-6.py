"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Brute Force: 
    # Use two nested loops to check every possible pair of bars, calculate the water volume for each pair, and keep track of the maximum . ->O(N^2)
class Solution:
    def maxArea(self,nums:List[int])->int:
        maximum = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                width = j-i
                height = min(nums[i],nums[j])
                current_water = height*width
                maximum = max(current_water,maximum)
        return maximum
                
# Optimal Solution
    # Goal : To save time complexity from O(N^2)-> O(1)
    # Keyword:  “Palindrome",”Target Sum”,“Getting Maxinum by array operation”  -> Basic Two pointer 
    # Approach: Two pointer Shrink from both ends to find the perfect fit
    # Tricks
        # When you're solving the water volume problem, always move the shorter pointer. It’s the only way to potentially find a higher bottleneck and increase the area
   
from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_water = 0
        while l < r:
            width = r-l
            height = min(heights[l],heights[r])
            current_water = height*width
            max_water =  max(current_water,max_water)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_water
# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable


def test():
    sol = Solution()
    result = sol.maxArea([1,7,2,5,4,7,3,6])
    print(f"Result: {result})")
if __name__ == "__main__":
    test()




