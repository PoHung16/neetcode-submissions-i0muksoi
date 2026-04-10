from typing import List
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        # Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
        # Image: Imagine an instant-lookup Map where you check if a Key or Value exists before , then perform following actions
        # Workflow - 3 Steps:
        # Step 1: Initialize a map, store the key-value pair
        # Step 2: Traverse the Array to check if a Key or Value exists before,, then perform following actions
        # Step 3: Return the result
        hashMap = {}
        for i , value in enumerate(nums):
            complement = target - value
            if complement in hashMap:
                return [hashMap[complement],i]
            hashMap[value] = i
        return []
  
def test():
    sol = Solution()
    nums = [3,4,5,6]
    target = 7
    result = sol.hasduplicate(nums,target)
    print(f"Result:{result}")
        
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N HashMap

























