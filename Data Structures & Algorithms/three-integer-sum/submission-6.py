"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[List[int]]
"""
# Keyword : “Palindrome", "Target Sum"  -> Basic Two pointer 
# Image : Two pointer Shrink from both ends to find the perfect fit
# Tricks:
    # Sorting is a great way to prep your data before applying a two-pointer approach.
    # If its 3 sum, Fix an anchor, then sweep with two pointers—shrinking from both ends while skipping the repeats.

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                curSum = nums[i] + nums[l] + nums[r]
                if curSum < 0:
                    l+=1
                elif curSum>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return res

def test():
    sol = Solution()
    result = sol.threeSum([-1,0,1,2,-1,-4])
    print(f"Result: {result})")
if __name__ == "__main__":
    test()


# Time complexity: O(N^2) 
    # Sort the array.... O(logN)
    # Nested loop to Traverse the array ... O(N^2)
# Space complexity:  O(M)....space for the output list.Where m is the number of triplets 



