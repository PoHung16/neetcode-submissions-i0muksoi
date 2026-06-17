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
    # 2D Array Situation
        # row = mid // n , col = mid % n 
    # Search in Rotated Sorted Array Situation
        # A. Check if the LEFT side is perfectly sorted (Compare nums[left] with nums[mid])
        # B. perform binary search on sorted side
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            #  Check if the LEFT side is perfectly sorted
            if nums[l] <= nums[mid]:
                # perform binary search on sorted side
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Target is here, shrink right
                else:
                    l = mid + 1  # Target is on the other side
            #  Otherwise, the RIGHT side must be perfectly sorted
            else:
                # perform binary search on sorted side
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Target is here, shrink left
                else:
                    r = mid - 1  # Target is on the other side

        return -1

# Time complexity: O(LogN) ...  Since its divided by h times, 2^h = n, h = logN
# Space complexity:  O(1)....create constant variable               

def test():
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    result = sol.search(nums,1)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()


