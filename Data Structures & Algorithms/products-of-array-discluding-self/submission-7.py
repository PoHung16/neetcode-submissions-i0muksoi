"""
 OOD: No
 Constraints: No
 input : List[int]
 output : List[int]
"""

# Brute Force: 
    # Multiply all other elements for each position using nested loops -> O(N^2)
class Solution:
    def productExceptSelf(self, nums:List[int])->List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            res.append(product)
        return res
# Optimal Soltion:
    # Keyword : "Contiguous Subarray" + "Negative Numbers" ->Prefix Sum + HashMap.
    # Keyword : “Except Self" -> PrefixProduct
    # Approach: Use Array to record prefix product and suffix product. One goes from left to right, and the other goes from right to left
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
# Time complexity: O(N) ... Traverse size N Array *2
# Space complexity:  O(1)....In place
def test():
    sol = Solution()
    nums = [1, 2, 3, 3]
    result = sol.productExceptSelf(nums)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()





