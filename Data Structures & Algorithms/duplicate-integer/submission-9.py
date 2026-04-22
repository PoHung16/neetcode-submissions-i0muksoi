"""
 OOD: No
 Constraints: No
 input : List[int]
 output : boolean
"""
# Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
# Image : Imagine an instant-lookup Map Traverse an array to check if a Key or Value exists before , then perform following actions
from typing import List
class Solution:
    def hasDuplicate(self, nums:List[int]) -> bool:
        hashMap = {}
        for i, value in enumerate(nums):
            if value in hashMap:
                return True            
            hashMap[value] = i
        return False
def test():
    sol = Solution()
    nums = [1, 2, 3, 3]
    result = sol.hasDuplicate(nums)
    print(f"Result:{result}")

if __name__ == "__main__":
    test()

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N HashMap



        



























