"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[int]
"""
# Brute Force: 
    # Array - Use nested loops to multiply all other elements except for itself  -> O(N^2)
class Solution:
    def productExceptSelf(self, nums:[List[int]]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    res[i] *= nums[j]
        return res

# Optimal Soltion:
    # Goal : O(N^2) / O(NlogN) -> O(N)
    # Keyword : “Except Self" -> PrefixProduct
    # Approach: Use Array to record prefix product and suffix product. One goes from left to right, and the other goes from right to left
# Jump to "Subarray Sum Equals K problem"  

from typing import List
class Solution:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        res = [1] * len(nums)
        prefixProduct = 1
        for i in range(len(nums)):
            res[i] = prefixProduct
            prefixProduct *= nums[i]
        suffixProduct = 1
        for j in range(len(nums)-1,-1,-1):
            res[j] *= suffixProduct
            suffixProduct *= nums[j]
        return res


# Time complexity: O(N) ... Traverse size N Array *2
# Space complexity:  O(1)....In place

def test():
    sol = Solution()
    nums = [1,2,4,6]
    result = sol.productExceptSelf(nums)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()



 