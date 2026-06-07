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
        # Put all number into hashset to achieve O(1) lookUp and then find the starter and the Longest consecutive sequence
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Step 1: 先排序 (Sorting 消耗 O(n log n))
        nums.sort()
        
        max_len = 1
        current_len = 1  # 代表當前 window 的長度
        
        # Step 2: 用單指標模擬滑動窗口，從第二個元素開始檢查
        for i in range(1, len(nums)):
            # 情況 A：如果數字跟前一個一樣，跳過不處理（不打破 window，也不增加長度）
            if nums[i] == nums[i - 1]:
                continue
                
            # 情況 B：連續數字，擴大 window
            if nums[i] == nums[i - 1] + 1:
                current_len += 1
            else:
                # 情況 C：數字中斷了！結算上一個 window，並重置 window 長度
                max_len = max(max_len, current_len)
                current_len = 1
                
        # 最後還要再比較一次，因為最長序列可能剛好在陣列的最末端
        return max_len(max_len, current_len)


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
                while current_num + 1 in hashset:
                    current_length +=1
                    current_num+=1
                longestLength = max(longestLength,current_length)
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


