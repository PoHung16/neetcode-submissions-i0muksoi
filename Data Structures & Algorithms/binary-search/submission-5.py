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
    # Find "minimum" in Rotated Sorted Array Situation: 
        # A. The squeeze use ""while l < r", the loop automatically stops when only one element being left. This will be mininum
        # B. We compare the mid value with nums[r] (Check which side is a normal slope), minimum will be on left side, otherwise  minimum will be on right side or itself . ps.[6,1,2]
from typing import List
class Solution:
    def search(self, nums:List[int],target:int) -> int:
        l, r = 0 , len(nums)-1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid +1
        return -1

 
def test():
    sol = Solution()
    nums = [-1,0,2,4,6,8]
    target= 4
    result = sol.search(nums,target)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()
    

# Time Complexity: O(logN) .... Since its divided by h times, 2^h = n, h = logN
# Space Complexity: O(1)... We didn't create extra variable or data structure       




        

        
        