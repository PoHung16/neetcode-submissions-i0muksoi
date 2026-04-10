from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Keyword : “Except Self" -> PrefixSum
        # Image : Imagine two passes. One goes left to right to collect prefix products, and the other goes right to left to collect suffix products
        # Workflow - 3 steps
        # Step 1:  Start with a Res array filled with 1s.
        # Step 2:  Go right to record the product of everything you've seen so far on the left. Go left to record the product of everything you've seen so far on the right. 
        # Step 3: Return the result
        res = [1] * len(nums)
        leftVal = 1
        for i in range(len(nums)):
            res[i] = leftVal
            leftVal *= nums[i]
        rightVal = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= rightVal
            rightVal *= nums[i]
        return res

def test():
    sol = Solution()
    nums = [1, 2, 3, 3]
    result = sol.productExceptSelf(nums)
    print(f"Result:{result}")
#Time complexity: O(N) ... Traverse size N Array *2
#Space complexity:  O(1)....In place




