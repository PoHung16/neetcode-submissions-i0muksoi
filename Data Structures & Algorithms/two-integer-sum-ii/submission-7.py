"""
 OOD: No
 Constraints: No
 input : List[int], int
 output : bool List[int]ean
"""
# Keyword : Two Sum -> but solution must use O(1) additional space -> cannot use hashmap
# Keyword : “Palindrome",”Target Sum”,“maximum area of water”  -> Basic Two pointer 
# Image : Two pointer Shrink from both ends to find the perfect fit
# Tricks:
    # Sorting is a great way to prep your data before applying a two-pointer approach.
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        l, r = 0, len(nums)-1
        while l < r:
            currentSum = nums[l] + nums[r]
            if currentSum < target:
                l+=1
            elif currentSum > target:
                r-=1
            else:
                return[l+1,r+1]
        return []

def test():
    sol = Solution()
    result = sol.twoSum([1,2,3,4],3)
    print(f"Result: {result})")
if __name__ == "__main__":
    test()

# Time complexity: O(NlogN) > O(N)
    # Sort: O(NlogN)
    # Traverse size N array: O(N)
    # O(NlogN) > O(N)
# Space complexity:  O(1)....create constant variable
