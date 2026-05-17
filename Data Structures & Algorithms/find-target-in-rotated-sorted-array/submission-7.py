"""
 OOD: No
 Constraints: Yes
 input : List[int],int
 output : int
"""
#Keyword : Search in Rotated Sorted Array -> Search in Rotated Sorted Array 
#Image :  Traverse the array with l, r pointer, and we compare the mid value with target, if equal we find it, it target is smaller, we search left side, if target is larger, we search the right side
# Tricks :  
    # use “=”, "l <= r” ensures the loop still runs when the search range shrinks to a single element.
    # Check which side is a normal slope to perform binary search:   if nums[l] <= nums[mid]:

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: #normal slope
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid +1 #右側
            else: #normal slope
                if nums[mid] < target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1
        return -1
# Time complexity: O(LogN) ...  Since its divided by h times, 2^h = n, h = logN
# Space complexity:  O(1)....create constant variable               


