"""
 OOD: No
 Constraints: No
 input : List[int], integer
 output : List[int]
"""
# Brute Force: 
    # Use nested loops to see if they add up to a target -> O(N^2)
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []

# Optimal Soltion:
    # Goal : O(N^2) / O(NlogN) -> O(N)
    # Keyword : “Two Sum", "Duplicate", "Frequency count", "Matching pairs", "Anagrams" -> Basic HashMap
    # Approach:  Use an O(1) HashMap to traverse array to check if a Key or Value exists before , then perform following actions
from typing import List
class Solution:
    def twoSum(self,nums: List[int], target: int)->List[int]:
        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement],i]
            hashMap[nums[i]] = i
        return []
# Time complexity: O(N) ... Traverse size N Array 
# Space complexity:  O(N)....create size N HashMap

def test():
    sol = Solution()
    nums = [3,4,5,6]
    target = 7
    result = sol.twoSum(nums,target)
    print(f"Result:result")

if __name__ == "__main__":
    test()










