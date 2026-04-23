"""
 OOD: No
 Constraints: No
 input : List[int]
 output : boolean
"""
# Keyword : “A consecutive sequence"-> Sliding Window , but sort will take O(nlogN) . it contradicts the constraints
# Keyword: O(1) lookUp -> HashSet
# Image:
    # brute force: 
        # Layer1 O(N): Traverse the array to check with number x can be starter
        # Layer2 O(N): Check if the consecutive sequence can reach x+1 or  x+2 or x+3 .... N個目標
        # Layer3 O(N): Every number if need O(N) to search in the array
    # optimal Solution
        # Put all number into hashset to achieve O(1) lookUp and then find Longest consecutive sequence

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)

        longestLength = 0
        for num in hashset:
            if (num - 1) not in hashset:
                current_num = num
                current_length = 1
                while current_num+1 in hashset:
                    current_length += 1
                    current_num+=1
                longestLength = max(longestLength, current_length)
        return longestLength

def test():
    sol = Solution()
    nums = [2,20,4,10,3,4,5]
    result = sol.longestConsecutive(nums)
    print(f"Result:{result}")
test()

if __name__ == "__main__":
    test()

# Time complexity: O(N) ... Traverse size N Array and Size N set
# Space complexity:  O(N)....create size N HashSet     
