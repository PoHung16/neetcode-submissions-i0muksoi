"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Brute Force: 
    # Array - Use two nested loops to check every possible pair of bars, calculate the water volume , and keep track of the maximum . ->O(N^2)
class Solution:
    def maxArea(self, nums:List[int])-> int:
        maxArea = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                width = j -i
                height = min(nums[i],nums[j])
                area = width * height
                maxArea = max(maxArea, area)
        return maxArea    
# Optimal Solution
    # Goal: O(N^2)->O(N) Two pointer technique : O(N^2)->O(N)
    # Keyword:  “Palindrome",”Target Sum”,“Getting Maxinum by array operation”  -> Basic Two pointer 
    # Approach: Two pointer Shrink from both ends to find the perfect fit
    # Tricks
        # When you're solving the water volume problem, always move the shorter pointer. It’s the only way to potentially find a higher bottleneck and increase the area

from typing import List
class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1
        maxArea = 0
        while l < r:
            width = r - l
            height = min(nums[l],nums[r])
            area = width * height
            maxArea = max(maxArea, area)
            if nums[l] < nums[r]:
                l+=1
            else:
                r-=1
        return maxArea    

# Time complexity: O(N) ...traverse size N array
# Space complexity:  O(1)....create constant variable


def test():
    sol = Solution()
    result = sol.maxArea([1,7,2,5,4,7,3,6])
    print(f"Result: {result})")
if __name__ == "__main__":
    test()






