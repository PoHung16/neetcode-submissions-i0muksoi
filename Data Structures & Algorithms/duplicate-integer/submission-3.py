class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Keyword : Search in Rotated Sorted Array -> Binary Search :  Search in Rotated Sorted Array 
        # Image : Imagine an instant-lookup Map where you check if a Key or Value exists before , if not add it into map
        # 3-Step Flow
        #Step 1:   Initialize a map, store the key-value pair
        seenMap = {}
        #Step 2:  Traverse the Array to  check if a  a Key or Value exists before, if not add it into map
        for num in nums:
            if num in seenMap:
                return True
            seenMap[num] = True
        #Step3: Return the result
        return False

# Time complexity: O(N) ... Traverse size N Array
# Space complexity:  O(N)....create size N Array
def test():
    sol = Solution()
    nums = [1, 2, 3, 3]
    result = sol.hasduplicate(nums)
    print(f"Result:{result}")