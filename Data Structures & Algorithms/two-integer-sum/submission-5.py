"""
 OOD: No
 Constraints: No
 input : List[int], integer
 output : boolean
"""
# Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
# Image : Imagine an instant-lookup Map Traverse an array to check if a Key or Value exists before , then perform following actions

from typing import List
class Solution:
    def twoSum(self,nums: List[int], target: int)->List[int]:
        hashMap = {}
        for i, value in enumerate(nums):
            complement = target - value
            if complement in hashMap:
                return [hashMap[complement],i]
            hashMap[value] = i
        return []
def test():
    sol = Solution()
    nums = [3,4,5,6]
    target = 7
    result = sol.twoSum(nums,target)
    print(f"Result:{result}")
if __name__ == "__main__":
    test()
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N HashMap








