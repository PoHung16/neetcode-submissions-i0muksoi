from typing import List
class Solution:
    # Keyword : “A consecutive sequence"-> Sliding Window , but sort will take O(nlogN) 
    # Keyword : "O(N) LoopUp to replace nested lookop" -> HashSet
    # Image: Imagine a Chain. To find the longest one, don't start from the middle. Use a HashSet as a Quick Scanner to find the Head of the chain (where num - 1 is missing), then just pull the whole thing out.
    # Step 1: Initialize a set, store all elements into set
    # Step 2: Traverse the hashset to check if num -1 exists before, then pull the whole thing out.
    # Step 3: Return the result
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            hashset.add(num)
        
        res = 0
        for num in hashset:
            if num -1 not in hashset: # 找到 Head
                length = 1
                current_num = num
                while current_num+1 in hashset:
                    length += 1
                    current_num +=1
                res = max(res, length)
            
        return res
def test():
    sol = Solution()
    nums = [2,20,4,10,3,4,5]
    result = sol.longestConsecutive(nums)
    print(f"Result:{result}")
test()
# Time complexity: O(N) ... Traverse size N Array and Size N set
# Space complexity:  O(N)....create size N HashSet        
