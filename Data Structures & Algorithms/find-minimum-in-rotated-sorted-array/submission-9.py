
"""
 OOD: No
 Constraints: Yes
 input : List[int],int
 output : int
"""
# Keyword : “Sorted Array " or "Sorted 2D martix" or "Search in rotated array" -> Basic Binary Search
# Image :  Traverse the array with l, r pointer
# Tricks :  
    # Common Situation: 
        # A. The squeeze use "while l <= r” ensures the loop still runs when the search range shrinks to a single element.
        # B. We compare the mid value with target, if equal we find it, it target is smaller, we search left side, if target is larger, we search the right side
    # Find "minimum" in Rotated Sorted Array Situation: 
        # A. The squeeze use ""while l < r", the loop automatically stops when only one element being left. This will be mininum
        # B. We compare the mid value with nums[r] (Check which side is a normal slope), minimum will be on left side, otherwise  minimum will be on right side or itself . ps.[6,1,2]
from typing import List
class Solution:
    def findMin(self, nums:List[int]) -> int:
        l, r = 0 , len(nums)-1
        while l < r:
            mid = (l+r) //2
            if nums[mid] > nums[r]: #left side is normal slope, and minumum will be on the right side
                l = mid + 1
            else:
                r = mid  #right side is normal slope, and minumum will be on on rightside or itself . ps.[6,1,2]
        return nums[l]


def test():
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    result = sol.findMin(nums)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

# Time complexity: O(LogN) ... Binary Search...Tree height
# Space complexity:  O(1)....create constant variable
