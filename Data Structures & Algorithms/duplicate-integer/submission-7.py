from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
        # Image: Imagine an instant-lookup Map where you check if a Key or Value exists before , then perform following actions
        # Workflow - 3 Steps:
        # Step 1: Initialize a map, store the key-value pair
        # Step 2: Traverse the Array to check if a Key or Value exists before,, then perform following actions
        # Step 3: Return the result
        hashMap = {}
        for i, num in enumerate(nums):
            if num in hashMap:
                return True
            hashMap[num] = i
        return False
def test():
    sol = Solution()
    nums = [1, 2, 3, 3]
    result = sol.hasduplicate(nums)
    print(f"Result:{result}")
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N HashMap

