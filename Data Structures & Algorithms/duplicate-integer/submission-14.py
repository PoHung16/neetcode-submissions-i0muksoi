"""
 OOD: No
 Constraints: No
 input : List[int]
 output : boolean
"""
# Brute Force: 
    # Compare every pair one by one using nested loop -> O(N^2)
class Solution:
    def hasDuplicate(self,nums:List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
# Optimal Solution
    # Keyword:  “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams"  -> Basic HashMap
    # Approach:  Use an O(1) HashMap to traverse array to check if a Key or Value exists before , then perform following actions
from typing import List
class Solution:
    def hasDuplicate(self,nums:List[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            hashMap[nums[i]] = i
        return False
# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N HashMap

def test():
    sol = Solution()
    nums = [1,2,3,3]
    result = sol.hasDuplicate(nums)
    print(f"result:{result}")
if __name__ == "__main__":
    test()



        



























