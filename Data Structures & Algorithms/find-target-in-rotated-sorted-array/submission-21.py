"""
 OOD: No
 Constraints: Yes
 input : List[int],int
 output : int
"""
# Brute Force: 
    # Traverse the array or use min function to min value in an array -> O(N)
from typing import List
class Solution: 
    def search(self, nums:List[int])->int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

# Optimal Solution
    # Goal: make O(N) search -> O(logN)
    # Keyword:  “Sorted Array " or "Sorted 2D matrix" or "Search in rotated array" -> Basic Binary Search
    # Approach: Traverse the array with l, r pointer with while loop to compare mid value with target, remember "=" to ensure the loop still runs when the search range shrinks to a single element
    # Tricks :  
        # Search in Rotated Sorted Array Situation
        # A. Check if the LEFT side is perfectly sorted (Compare nums[left] with nums[mid])
        # B. perform binary search on sorted side
    
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]: # left side is perfectly sorted
                if nums[l] <= target < nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1
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


