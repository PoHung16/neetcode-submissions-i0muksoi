"""
 OOD: No
 Constraints: Yes
 input : List[int],int
 output : int
"""
# Keyword : “Sorted Array" -> Basic Binary Search
# Image :  Traverse the array with l, r pointer, and we compare the mid value with target, if equal we find it, it target is smaller, we search left side, if target is larger, we search the right side
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            mid_idex = (l + r) //2
            if target == nums[mid_idex]:
                return mid_idex
            elif target < nums[mid_idex]:
                r = mid_idex -1
            elif target > nums[mid_idex]:
                l = mid_idex +1
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




        

        
        