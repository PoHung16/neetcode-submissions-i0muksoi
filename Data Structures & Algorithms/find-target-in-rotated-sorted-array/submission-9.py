"""
 OOD: No
 Constraints: Yes
 input : List[int],int
 output : int
"""
# Keyword : “Sorted Array " or "Sorted 2D matrix" or "Search in rotated array" -> Basic Binary Search
# Image :  Traverse the array with l, r pointer
# Tricks :  
    # Common Situation: 
        # A. The squeeze use "while l <= r” ensures the loop still runs when the search range shrinks to a single element.
        # B. We compare the mid value with target, if equal we find it, it target is smaller, we search left side, if target is larger, we search the right side
        # B-2. Identify the cliff (Rotated Array):  We compare the mid value with nums[r] , if mid value is greater, left side is normal slope
        # C. Shrink:  In normal slope side, we perform binary search
    # Find "minimum" in Rotated Sorted Array Situation: 
        # A. The squeeze use ""while l < r", the loop automatically stops when only one element being left. This will be mininum
        # B. Identify the cliff (Rotated Array):  We compare the mid value with nums[r] , if mid value is greater, left side is normal slope
        # C. Shrink: If left side is normal slope,  minimum will be on right side. Otherwise,  minimum will be on left side or itself  ps.[6,1,2]
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[r]: # left side is noraml slope
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1 # on the other side
            else: # right side is noraml slope
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
        return -1

def test():
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    result = sol.search(nums,1)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

# Time complexity: O(LogN) ...  Since its divided by h times, 2^h = n, h = logN
# Space complexity:  O(1)....create constant variable               


