"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[int]
"""
# Keyword : “Except Self" -> PrefixSum
# Image: Use Array to record prefix product and suffix product. One goes from left to right, and the other goes from right to left

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftVal = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = leftVal
            leftVal *= nums[i]
        rightVal = 1
        for j in range(len(nums)-1,-1,-1):
            res[j] *= rightVal
            rightVal *= nums[j]
        return res

def test():
    sol = Solution()
    nums = [1, 2, 3, 3]
    result = sol.productExceptSelf(nums)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()
#Time complexity: O(N) ... Traverse size N Array *2
#Space complexity:  O(1)....In place




