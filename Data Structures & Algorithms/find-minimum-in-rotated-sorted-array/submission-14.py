
"""
 OOD: No
 Constraints: Yes
 input : List[int]
 output : int
"""
# Brute Force: 
    # Array - Traverse the array or use min function to get min value in an array -> O(N)
from typing import List
class Solution: 
    def findMin(self, nums:List[int])->int:
        minumum = min(nums)
        return minumum

# Optimal Solution
    # Goal: make O(N) search -> O(logN)
    # Keyword:  “Sorted Array " or "Sorted 2D matrix" or "Search in rotated array" -> Basic Binary Search
    # Approach: 
        # 1. Two pointer to Get "Mid" to decide search on which side. Diffrent from 2 pointer, while l<=r ,remember "=" to ensure the loop still runs when the search range shrinks to a single element
    # Tricks :  
        # Find "minimum" in Rotated Sorted Array Situation:
        # A. Squeeze range using "while l < r": The loop stops automatically when only one element is left (the minimum).
        # B. Check the minimum value lies in the left half or the right half of the array.
from typing import List
class Solution:
    def findMin(self, nums:List[int]) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:  #minimum is at the right side
                l = mid + 1
            else: #minimum is at the left side or itself
                r = mid 
        return nums[l] # return the last element

    
# Time complexity: O(LogN) ... Binary Search...Tree height
# Space complexity:  O(1)....create constant variable
def test():
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    result = sol.findMin(nums)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

