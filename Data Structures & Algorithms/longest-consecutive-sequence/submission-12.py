"""
 OOD: No
 Constraints: No
 input : List[int]
 output : int
"""
# Keyword : “A consecutive sequence"-> Sliding Window , but sort will take O(nlogN) . it contradicts the constraints
# Image: Sort it first and then traverse an array to expand current window size until it meets a condition, then update the max window size and reset current window size
# Tricks:
    # You will need to compare max window size and current window one last time after the for loop cuz the longest consecutive string might be at the end of the array
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_window_size = 1
        current_window_size = 1
        for i in range(1,len(nums)):
            # 情況 A：如果數字跟前一個一樣，跳過不處理（不打破 window，也不增加長度）
            if nums[i] == nums[i-1]:
                continue
            # 情況 B：連續數字，擴大 window
            if nums[i] == nums[i-1]+1:
                current_window_size+=1
            # 情況 C：數字中斷了！結算max window，並重置 window 長度
            else:
                max_window_size = max(max_window_size,current_window_size)
                current_window_size =1
        return max(max_window_size, current_window_size)

# Way2: 
# Keyword: O(1) lookUp -> HashSet
# Image:
    # optimal Solution
        # Put all number into hashset to achieve O(1) lookUp and then find the starter and the Longest consecutive sequence

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashSet = set()
        for num in nums:
            hashSet.add(num)
        max_length = 1
        for num in hashSet:
            if (num-1) not in hashSet:
                current_num = num
                current_length = 1
                while current_num+1 in hashSet:
                    current_num+=1
                    current_length+=1
                max_length = max(max_length,current_length)

        return max_length
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


